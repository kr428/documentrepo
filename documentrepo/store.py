"""document repository"""


class store:
    """store implementation"""

    documents = {}

    def __init__(self):
        self.documents["1"]="foo"
        self.documents["2"]="bar"
        self.documents["3"]="baz"

    def list_docs(self):
        return self.documents

    def get_document(self,doc):
        return self.documents[doc]