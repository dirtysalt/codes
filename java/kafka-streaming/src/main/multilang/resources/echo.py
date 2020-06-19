import storm
import sys
class EchoBolt(storm.BasicBolt):
    def process(self, tup):
        values = tup.values
        # can not use stdout here
        sys.stderr.write("tuple size = %d, output by echo2bolt: %s\n" % (len(values), values))
        words = tup.values
        storm.emit(words)

bolt = EchoBolt()
bolt.run()