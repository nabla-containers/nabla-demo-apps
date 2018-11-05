FROM golang

COPY src/ /goapp/
WORKDIR "/goapp"

RUN go get -d ./...
RUN go build

ENTRYPOINT ["/goapp/goapp"]

