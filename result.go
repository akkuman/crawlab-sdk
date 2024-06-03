package sdk

import (
	"context"
	"encoding/json"
	"io"

	grpc "github.com/crawlab-team/crawlab-grpc"
	"github.com/crawlab-team/crawlab-sdk/entity"
	"github.com/crawlab-team/crawlab-sdk/interfaces"
	"github.com/crawlab-team/go-trace"
)

var RS *ResultService

type ResultService struct {
	// internals
	sub grpc.TaskService_SubscribeClient
}

func (svc *ResultService) SaveItem(items ...entity.Result) {
	svc.save(items)
}

func (svc *ResultService) SaveItems(items []entity.Result) {
	svc.save(items)
}

func (svc *ResultService) save(items []entity.Result) {
	var _items []entity.Result
	for i, item := range items {
		_items = append(_items, item)
		if i > 0 && i%50 == 0 {
			svc._save(_items)
			_items = []entity.Result{}
		}
	}
	if len(_items) > 0 {
		svc._save(_items)
	}
}

func (svc *ResultService) _save(items []entity.Result) {
	// skip if no task id specified
	if GetTaskId().IsZero() {
		return
	}

	var records []interface{}
	for _, item := range items {
		item["_tid"] = GetTaskId()
		records = append(records, item)
	}
	data, err := json.Marshal(&entity.StreamMessageTaskData{
		TaskId:  GetTaskId(),
		Records: records,
	})
	if err != nil {
		trace.PrintError(err)
		return
	}
	if err := svc.sub.Send(&grpc.StreamMessage{
		Code: grpc.StreamMessageCode_INSERT_DATA,
		Data: data,
	}); err != nil {
		trace.PrintError(err)
		return
	}
}

func (svc *ResultService) init() (err error) {
	c := GetClient()
	taskClient := c.GetTaskClient()
	svc.sub, err = taskClient.Subscribe(context.Background())
	if err != nil {
		return trace.TraceError(err)
	}
	return nil
}

func GetResultService(opts ...ResultServiceOption) interfaces.ResultService {
	if RS != nil {
		return RS
	}

	// service
	svc := &ResultService{}

	// apply options
	for _, opt := range opts {
		opt(svc)
	}

	// initialize
	if err := svc.init(); err != nil {
		panic(err)
	}

	RS = svc

	return svc
}

func SaveItem(items ...entity.Result) {
	GetResultService().SaveItem(items...)
}

func SaveItems(items []entity.Result) {
	GetResultService().SaveItems(items)
}

// WaitStreamCloseAndRecv Wait for the message to be sent and the server to finish processing the sent data, then close the connection
// Note: It should be called before the program ends, waiting for the server to process all the data sent. 
// For example:
// func main() {
// 	defer sdk.WaitStreamCloseAndRecv()
// 	// some other handle...
// }
func WaitStreamCloseAndRecv() {
	if RS == nil {
		return
	}
	_, err := RS.sub.CloseAndRecv()
	if err != nil && err != io.EOF {
		trace.PrintError(err)
		return
	}
	RS = nil
}
