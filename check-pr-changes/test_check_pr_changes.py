from .check_pr_changes import Filter, Filters, filter_matches


def test_filter_matches() -> None:
    paths = ["check", ""]
    args_list = [[]]
    for args in args_list:
        filter_matches(*args)
