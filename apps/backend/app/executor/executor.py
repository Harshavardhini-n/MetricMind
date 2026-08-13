from app.registry.tool_registry import ToolRegistry
from app.catalog.catalog import SemanticCatalog


class Executor:

    METRICS = {
        "revenue": "revenue",
        "profit": "profit",
        "margin": "margin",
        "cost": "cost",
    }

    PERIOD_MAP = {
        "q1": "q1",
        "q2": "q2",
        "q3": "q3",
        "q4": "q4",

        "first quarter": "q1",
        "second quarter": "q2",
        "third quarter": "q3",
        "fourth quarter": "q4",

        "1st quarter": "q1",
        "2nd quarter": "q2",
        "3rd quarter": "q3",
        "4th quarter": "q4",
    }

    # ==========================================================
    # METRIC EXTRACTION
    # ==========================================================

    @classmethod
    def _extract_metric(cls, question):

        question = question.lower()

        for metric in cls.METRICS:

            if metric in question:
                return metric

        return None

    # ==========================================================
    # DIMENSION EXTRACTION
    # ==========================================================

    @classmethod
    def _extract_dimension(cls, question):

        question = question.lower()

        for dimension in SemanticCatalog.get_dimensions():

            if dimension.lower() in question:
                return dimension.lower()

        return None

    # ==========================================================
    # PERIOD EXTRACTION
    # ==========================================================

    @classmethod
    def _extract_period(cls, question):

        question = question.lower()

        # Longer phrases first
        periods = sorted(
            cls.PERIOD_MAP.items(),
            key=lambda item: len(item[0]),
            reverse=True,
        )

        for phrase, period in periods:

            if phrase in question:
                return period

        return None

    # ==========================================================
    # SINGLE METRIC
    # ==========================================================

    @classmethod
    def execute(
        cls,
        tool,
        question,
    ):

        tool_class = ToolRegistry.get_tool(tool)

        if not tool_class:
            return None

        metric = cls._extract_metric(question)

        if not metric:
            return None

        dimension = cls._extract_dimension(question)

        period = cls._extract_period(question)

        print("========================================")
        print("EXECUTOR - SINGLE METRIC")
        print("Metric:", metric)
        print("Dimension:", dimension)
        print("Period:", period)
        print("========================================")

        return tool_class.query_metric(
            metric=metric,
            dimension=dimension,
            period=period,
        )

    # ==========================================================
    # COMPARISON
    # ==========================================================

    @classmethod
    def compare(
        cls,
        tool,
        question,
    ):

        tool_class = ToolRegistry.get_tool(tool)

        if not tool_class:
            return None

        metric = cls._extract_metric(question)

        if not metric:
            return None

        period = cls._extract_period(question)

        print("========================================")
        print("EXECUTOR - COMPARISON")
        print("Metric:", metric)
        print("Period:", period)
        print("========================================")

        return tool_class.compare_metric(
            metric=metric,
            period=period,
        )

    # ==========================================================
    # RANKING
    # ==========================================================

    @classmethod
    def rank(
        cls,
        tool,
        question,
    ):

        tool_class = ToolRegistry.get_tool(tool)

        if not tool_class:
            return None

        metric = cls._extract_metric(question)

        if not metric:
            return None

        question_lower = question.lower()

        mode = "max"

        lowest_keywords = [
            "lowest",
            "least",
            "minimum",
            "min",
            "smallest",
            "worst",
            "bottom",
        ]

        for word in lowest_keywords:

            if word in question_lower:
                mode = "min"
                break

        period = cls._extract_period(question)

        print("========================================")
        print("EXECUTOR - RANKING")
        print("Metric:", metric)
        print("Mode:", mode)
        print("Period:", period)
        print("========================================")

        return tool_class.rank_metric(
            metric=metric,
            mode=mode,
            period=period,
        )