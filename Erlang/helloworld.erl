-module(helloworld).
-export([hi/0, hi/1]).


hi() ->
	io:format("Hello, world!~n").
hi([]) ->
	ok;
hi([Name | Rest]) -> 
	io:format("Hello, ~w~n", [Name]),
	hi(Rest).

