from resumer.infrastracture.helper.text_file_to_list import text_file_to_list


def test_text_file_to_list():
    file_path = "resumer/data/test/infrastracture/helper/write_profile.txt"
    assert text_file_to_list(file_path) == ["aiueo\n", "kakikukeko"]
