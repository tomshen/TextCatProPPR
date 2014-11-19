PROPPR_PATH = /remote/curtis/tomshen/ProPPR
PWD = $(shell pwd)

all: compile run

clean:
	$(PROPPR_PATH)/scripts/clean.sh .

compile:
	cd $(PROPPR_PATH) && ./scripts/compile.sh $(PWD) && cd $(PWD)

run:
	cd $(PROPPR_PATH) && java -cp '.:bin/:lib/*:conf/' \
	edu.cmu.ml.praprolog.Experiment --programFiles $(shell cat programFiles.arg) \
	--train $(PWD)/train.data --output $(PWD)/train.cooked \
	--test $(PWD)/test.data --params $(PWD)/params.wts --prover dpr:0.0001:0.01:boost \
	--threads 24 && cd $(PWD)

data:
	./process.py

.PHONY: all clean compile run data
