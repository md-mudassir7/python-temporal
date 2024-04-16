package server

import (
	"net/http"

	"github.com/gorilla/mux"
)

type routeEntry struct {
	path       string
	hFunc      http.HandlerFunc
	method     string
	nsRequired bool
}

type RouteTable map[string][]routeEntry

var ServiceRoutes RouteTable = RouteTable{
	"/health": []routeEntry{
		{"/health", health, http.MethodGet, false},
	},
}

func setAllRoutes(r *mux.Router) {
	for _, sr := range ServiceRoutes {
		for _, route := range sr {
			r.HandleFunc(route.path, route.hFunc).Methods(route.method)
			if route.method != http.MethodOptions {
				r.HandleFunc(route.path, handleOptions).Methods(http.MethodOptions)
			}
		}
	}
}

func handleOptions(w http.ResponseWriter, r *http.Request) {
	w.WriteHeader(http.StatusOK)
}
