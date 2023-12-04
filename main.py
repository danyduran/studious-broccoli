from data_capture import DataCapture

if __name__ == "__main__":
    capture = DataCapture()
    capture.add(3)
    capture.add(3)
    capture.add(4)
    capture.add(4)
    capture.add(5)
    capture.add(6)
    capture.add(6)
    capture.add(9)

    stats = capture.build_stats()
    assert stats.less(4) == 2
    assert stats.between(3, 6) == 7
    assert stats.greater(4) == 4
