class CardInfo:
    def __init__(self, conclusion: str, date: str, diagnosisName: str, doctor: str, hasChain: bool, hasNested: bool, id: str, previousId: str):
        self.conclusion = conclusion
        self.date = date
        self.diagnosisName = diagnosisName
        self.doctor = doctor
        self.hasChain = hasChain
        self.hasNested = hasNested
        self.id = id
        self.previousId = previousId

incomplete_testing_data = [CardInfo("Смерть",
                                    "06.11.2024",
                                    "Остеопороз с патологическим переломом после удаления яичников",
                                    "Доктор Анестезиолог-реаниматологг",
                                    0, 0,
                                    "6911d81c-30d7-4c5b-ba72-08dcfe20c9d6",
                                    None),
                           CardInfo("Болезнь",
                                    "30.06.2024",
                                    "Аборт неуточненный неполный, осложнившийся длительным или чрезмерным кровотечением",
                                    "hendo",
                                    1, 1,
                                    "3109a33d-8956-41d0-7161-08dc9a4cb881",
                                    None)
                           ]

division_into_equivalence_classes = [
    CardInfo("Смерть", "06.11.2025", "Остеопороз", "Доктор Дре", 0, 0, "6911d81c-30d7-4c5b-ba72-08dcfe20c9d6", None),
    CardInfo("Болезнь", "30.06.2024", "Абортище", "hendo", 1, 1, "3109a33d-8956-41d0-7161-08dc9a4cb881", None),
    CardInfo("Выздоровление", "01.08.2024", "Денге", "Доктор Анестезиолог", 0, 1, "0f7450e0-841c-40cf-7162-08dc9a4cb881", "3109a33d-8956-41d0-7161-08dc9a4cb881"),
    CardInfo("Выздоровление", "01.08.2024", "Денге", "Доктор Анестезиолог", 1, 0, "213949be-8ae9-49e6-79e0-08dc99c44493", None),
    CardInfo("Болезнь", "06.11.2025", "Остеопороз", "Доктор Дре", 0, 0, "6911d81c-30d7-4c5b-ba72-08dcfe20c9d6", "3109a33d-8956-41d0-7161-08dc9a4cb881"),
]

guessing_errors_data = [
    CardInfo("", "01.01.2024", "Заболевание 1", "", 0, 0, "1", ""),
    CardInfo("NoExist", "02.01.2024", "Заболевание 2", "Доктор 2", 0, 0, "2", "invalid-id"),
]

сlasses_of_bad_data_data = [
    [CardInfo(None, None, None, None, 0, 0, None, None)],
    [CardInfo("Выздоровление", "", "Заболевание 1", "Доктор 1", 0, 0, 123, None)],
    [CardInfo(1, "01.01.2024", "Заболевание 1", "Доктор 1", "yes", 0, 123, None)],
]

сlasses_of_good_data_data = [
        CardInfo("Выздоровление", "01.01.2024", "Заболевание 1", "Доктор 1", 0, 0, "1", None),
        CardInfo("Болезнь", "02.01.2024", "Заболевание 2", "Доктор 2", 1, 0, "2", None),
        CardInfo("Смерть", "03.01.2024", "Заболевание 3", "Доктор 3", 0, 1, "3", None),
        CardInfo("Выздоровление", "01.01.2024", "Заболевание 1", "Доктор 1", 0, 0, "1", None),
        CardInfo("Выздоровление", "01.01.2024", "Заболевание 1", "Доктор 1", 1, 1, "1", "0"),
        CardInfo("Болезнь", "02.01.2024", "Заболевание 2", "Доктор 2", 1, 1, "2", "1"),
        CardInfo("Смерть", "03.01.2024", "Заболевание 3", "Доктор 3", 1, 1, "3", "2"),
        CardInfo("Выздоровление", "04.01.2024", "Заболевание 4", "Доктор 4", 1, 1, "4", "3"),
        CardInfo("Болезнь", "05.01.2024", "Заболевание 5", "Доктор 5", 1, 1, "5", "4"),
]

testing_on_data_streams_data = [
    CardInfo("Выздоровление", "01.01.2024", "Заболевание 1", "Доктор 1", 0, 0, "1", None),
    CardInfo("Болезнь", "02.01.2024", "Заболевание 2", "Доктор 2", 1, 0, "2", None),
    CardInfo("Смерть", "03.01.2024", "Заболевание 3", "Доктор 3", 0, 1, "3", "2"),
    CardInfo("Выздоровление", "01.01.2024", "Заболевание 1", "Доктор 1", 0, 0, "1", None),
]