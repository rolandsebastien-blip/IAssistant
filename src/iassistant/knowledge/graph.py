class KnowledgeGraph:
    """
    Represents IAssistant's mental representation of the home.

    It stores every known object and every relationship
    between those objects.
    """

    def __init__(self) -> None:
        self._nodes = {}
        self._relationships = []