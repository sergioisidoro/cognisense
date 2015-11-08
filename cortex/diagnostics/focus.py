from cortex.api.event_stream import raw_event_stream
from pybrain.structure import RecurrentNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure import TanhLayer
from pybrain.datasets import SupervisedDataSet
import redis
import csv
import simplejson as json
# Train Neural network


class FocusNeuralNetork:
    def __init__(self):
        labels = ["tp9", "fp1", "fp2", "tp10"]

        print "creating nerual network"

        # 4 Channles, 1 output
        ds = SupervisedDataSet(4, 1)
        self.net = buildNetwork(4, 5, 1, bias=True, hiddenclass=TanhLayer)
        self.trainer = BackpropTrainer(self.net, ds)

        print "Creating Dataset"
        with open('cortex/diagnostics/data/focus/focused.csv', 'rb') as csvf:
            data = csv.reader(csvf, delimiter=',', quotechar='"')
            for row in data:
                if row[1] == ' /muse/eeg':
                    ds.addSample(
                        (float(row[2]), float(row[3]), float(row[4]),
                         float(row[5])),
                        (1,))

        with open('cortex/diagnostics/data/focus/relaxed.csv', 'rb') as csvf:
            data = csv.reader(csvf, delimiter=',', quotechar='"')
            for row in data:
                if row[1] == ' /muse/eeg':
                    ds.addSample(
                        (float(row[2]),
                         float(row[3]),
                         float(row[4]),
                         float(row[5])),
                        (0,))

        print "Training"
        self.trainer.trainEpochs(epochs=5)
        print "Automatic diagnostics are ready !!"

    def run(self):
        red = redis.StrictRedis()
        self.stream = raw_event_stream('patient1')
        while True:
            for message in self.stream:
                if message != 1:
                    message = json.loads(message)
                    # Build input
                    for data_point in message:
                        if message['type'] == 'EEG':
                            for i in range(len(message['timestamps'])):
                                nn_input = [message['tp9'][i],
                                            message['fp1'][i],
                                            message['fp2'][i],
                                            message['tp10'][i],
                                            ]
                                last_result = self.net.activate(nn_input)
                    print last_result[0]
                    red.publish("patient1_focus", last_result)
