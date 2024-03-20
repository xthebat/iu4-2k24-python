import shlex

import pytest

import extras

large_file_name = "large_file.txt"
middle_file_name = "middle_file.txt"

small_file_name = "small_file.txt"
small_file_text = "bind \"ins\" \"bot_place\""


def test_readfile_simple():
    filepath = extras.get_filepath(small_file_name)

    # Bad sample
    fp = open(filepath, "rt")
    text = fp.read()
    fp.close()

    assert text == small_file_text


def test_readfile_context_manager():
    filepath = extras.get_filepath(small_file_name)

    with open(filepath, "rt") as fp:
        text = fp.read()
        # Should be out of with but placed here for sample
        assert text == small_file_text


def test_readfile_try_finally():
    filepath = extras.get_filepath(small_file_name)

    fp = open(filepath, "rt")
    try:
        text = fp.read()
        # Should be out of try-finally but placed here for sample
        assert text == small_file_text
    finally:
        fp.close()


def test_readfile_try_finally_raise():
    filepath = extras.get_filepath(small_file_name)

    has_finally = False
    fp = open(filepath, "rt")
    with pytest.raises(AssertionError):
        try:
            text = fp.read()
            assert text == "crap"
        finally:
            fp.close()
            has_finally = True

    assert has_finally


def test_readfile_lines():
    filepath = extras.get_filepath(middle_file_name)

    with open(filepath, "rt") as fp:
        not_blank_lines = [line.strip() for line in fp.readlines() if line.strip()]

    actual = "\n".join(not_blank_lines)
    expected = """// CSGO-GSB5D-8Lup2-WxHJG-Wvv3i-vSLoD  default
// CSGO-8LOzV-Gfifq-XnyOm-iK3XA-bkpNO
clear
viewmodel_presetpos 0
viewmodel_fov 68
viewmodel_offset_x 2.5
viewmodel_offset_y 0.0
viewmodel_offset_z -2.0
cl_usenewbob false
// viewmodel_presetpos 0
// viewmodel_fov 54  // 68
// viewmodel_offset_z -2  // -1.5
fps_max 220
// m_rawinput 1
// net_maxroutable 1200
// cl_cmdrate 128
// cl_updaterate 128
// rate 786432
alias +fast_forward_time "host_timescale 10"
alias -fast_forward_time "host_timescale 1"
alias +normal_hud_scale "hud_scaling 0.80"
alias -normal_hud_scale "hud_scaling 0.40"
alias "toggle_hud_scale" "small_hud_scale"
alias "small_hud_scale" "-normal_hud_scale; alias toggle_hud_scale large_hud_scale"
alias "large_hud_scale" "+normal_hud_scale; alias toggle_hud_scale small_hud_scale"
alias +right_hand "cl_righthand 1"
alias -right_hand "cl_righthand 0"
alias "toggle_right_hand" "right_hand_enable"
alias "right_hand_enable" "-right_hand; alias toggle_right_hand right_hand_disable"
alias "right_hand_disable" "+right_hand; alias toggle_right_hand right_hand_enable\""""
    assert actual == expected


# TODO: capsys
def test_readfile_lines_alias():
    filepath = extras.get_filepath(middle_file_name)

    def _test_func(_line: str):
        print(f"From test func: {_line}")
        return _line.strip()

    with open(filepath, "rt") as fp:
        aliases = [_test_func(line) for line in fp.readlines() if line.startswith("alias")]

    for it in aliases:
        print(it)

    print("<=====================================================================>")

    with open(filepath, "rt") as fp:
        aliases = (_test_func(line) for line in fp.readlines() if line.startswith("alias"))

    for it in aliases:
        print(it)


def test_readfile_bind():
    filepath = extras.get_filepath(large_file_name)

    def split_outside_quotes(item: str):
        item = item.replace("\\", "\\\\")
        return shlex.split(item)

    def remove_quotes(item: str) -> str:
        return item.removeprefix("\"").removesuffix("\"")

    with open(filepath, "rt") as fp:
        binds = (split_outside_quotes(it) for it in fp.readlines() if it.startswith("bind"))
        binds = {remove_quotes(it[1]): remove_quotes(it[2]) for it in binds}

    for k, v in binds.items():
        print(f"{k}: {v}")
