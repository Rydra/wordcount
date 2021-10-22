from hamcrest import *

from wordcount.counter import most_frequent_words


def test_count_the_words_of_the_lorem_ipsum():
    results = most_frequent_words("resources/content.txt", top_n=3)

    assert_that(
        results, has_length(3)
    )

    assert_that(
        results, contains_exactly(
            has_properties(word="in", line_appearances=[3, 4, 7, 26, 30, 33, 37, 39], num_appearances=11),
            has_properties(word="sed", line_appearances=[5, 17, 19, 21, 22, 23, 34, 37, 41], num_appearances=10),
            has_properties(word="ut", line_appearances=[1, 4, 13, 19, 21, 24, 30, 32, 34], num_appearances=9),
        )
    )
