import struct

class Record_ModuleName_65532:
    fields = ['text']
    message_type = 65532
    label = 'Record_ModuleName'
    _length = -1
    verboseOnly = False
    payload = []
    data = {}

    def __init__(self, payload):
        if type(payload) == bytes:
            self.data = self.parse(payload.decode(encoding='UTF-8', errors='backslashreplace'))
            return
        self.data = self.parse(payload)

    @classmethod
    def parse(self, payload):
        data = {'text': payload}
        return data