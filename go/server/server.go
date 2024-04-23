// nolint:staticcheck,funlen,ineffassign,misspell,govet,dupl,unused,gosimple,gocritic,gocyclo,errcheck,revive,bodyclose,unconvert
package server

import (
	"context"
	"net/http"
	"sync"
	"time"

	"log"

	"github.com/gorilla/mux"
)

var (
	server *Server
	once   sync.Once
)

type Server struct {
	srv *http.Server
	r   *mux.Router
}

func init() {
	once.Do(func() {
		server = &Server{}
		server.r = mux.NewRouter()
	})
}

func health(w http.ResponseWriter, r *http.Request) {
	log.Println("Recived health check request", r)
	w.Write([]byte("Server is healthy!!!!"))
}

func Start() {
	// initialise tracer

	server.r = mux.NewRouter()
	setAllRoutes(server.r)
	log.Println("Starting server")
	server.srv = &http.Server{Addr: ":3000", Handler: server.r}

	go func() {
		err := server.srv.ListenAndServe()
		log.Println("server.srv.ListenAndServe Failed", "error", err)
	}()

	func() {
		for {
			time.Sleep(1 * time.Second)
		}
	}()
}

func Stop() {
	server.srv.Shutdown(context.Background())
}
