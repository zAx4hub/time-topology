from time_topology.engine import demo, inspect, rank, run, similarity


def test_rank_deterministic():
    assert rank("hello zax world", 7) == rank("hello zax world", 7)
    assert rank("", 1) == 0


def test_similarity():
    assert similarity("a b", "a b") == 1
    assert similarity("a", "z") == 0


def test_run():
    r = run({"items": [{"text": "alpha"}, {"text": "beta gamma"}], "threshold": 0.01})
    assert "zAx4hub" in r["author"]
    assert r["project"] == "time-topology"
    assert len(r["findings"]) == 2


def test_demo_inspect():
    assert demo()["score"] >= 0
    assert inspect()["name"] == "time-topology"
