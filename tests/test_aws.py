from systems import aws


def test_create_single_instances():
    single_fetcher_settings = dict(
        name="single_test",
        repetition=1,
        parallel_fetcher=1
    )
    single_id_in_list = aws.create_instance(single_fetcher_settings)
    print(single_id_in_list)

    assert len(single_id_in_list) == 1


def test_create_multiple_instances():
    multiple_fetcher_settings = dict(
        name="multi_test",
        repetition=1,
        parallel_fetcher=4
    )
    multi_ids = aws.create_instance(multiple_fetcher_settings)
    print(multi_ids)

    assert len(multi_ids) == 4

