from src.n_ary_tree.encode_decode_tree import decode, encode
from tests.test_helpers.test_helpers import get_n_ary_tree_values, get_n_nary_tree


def test_encode_decode():
    tree = get_n_nary_tree()
    values = get_n_ary_tree_values(tree)
    encoded_tree = encode(tree)
    assert encoded_tree is not None

    decoded_tree = decode(encoded_tree)
    assert decoded_tree is not None
    assert get_n_ary_tree_values(decoded_tree) == values
