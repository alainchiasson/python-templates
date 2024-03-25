from cat import main


def test_single_file(capsys, tmp_path):
    file = tmp_path / "test.txt"
    file.write_text("Hello world!\n")

    result = main([str(file)])

    assert result == 0
    out, err = capsys.readouterr()
    assert out == "Hello world!\n"
    assert err == ""


def test_single_file_with_numbering(capsys, tmp_path):
    file = tmp_path / "test.txt"
    file.write_text("Hello world!\n")

    result = main(["-n", str(file)])

    assert result == 0
    out, err = capsys.readouterr()
    assert out == "     1 Hello world!\n"
    assert err == ""
