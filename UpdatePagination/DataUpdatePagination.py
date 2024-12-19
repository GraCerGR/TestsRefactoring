
incomplete_testing_data = [[4, 5],[5, 7],[0, 7],[7, 0]]

structured_baseline_testing = [[1, 1],[2, 3],[5, 5],
                               [1, 10],[2, 20],[3, 50],
                               [5, 10],[6, 10],[7, 11],
                               [8, 10],[9, 10],[10, 10]]

testing_on_data_streams_data = structured_baseline_testing + [[0, 10], [10, 9], [10, 0]]

division_into_equivalence_classes = testing_on_data_streams_data

guessing_errors_data = [[-1, 0], [0, -1], [0, 0], ["Два", 3], [4, "Два"]]

analysis_of_boundary_values = [[1, 4],[2, 5],[5, 6],
                               [2, 7],[3, 7],[4, 7],
                               [7, 10],[8, 10],[9, 10],
                               [-1, 5],[0, 5],[1, 5],
                               [-1, -1],[0, 0],[1, 1]]

сlasses_of_bad_data_data = [[None, None],[None, 5],[4, None],
                            ["FFF", 5],[5, "FFF"],[2.75, "*"],
                            [-10, -5],[-3, 5],[6, -6]]

сlasses_of_good_data_data = structured_baseline_testing + [[1, 1], [500, 1000]]
