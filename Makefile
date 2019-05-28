.PHONY: analysis-build analysis collector-build collector converter-build

build: analysis-build 

collector-build:
	docker build -t cbor-tls-collector collector/

collector:
	docker run --rm -v ${PWD}/data:/data cbor-tls-collector

converter-build:
	docker build -t cbor-tls-converter converter/

analysis-build:
	docker build -t cbor-tls-analysis analysis/

analysis:
	docker run --rm -v ${PWD}/analysis:/analysis -v ${PWD}/data:/data cbor-tls-analysis
