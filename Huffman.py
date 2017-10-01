def Table(str):
    frequency_table = {}
    for chr in str:
        cur_freq = frequency_table[chr]
        if cur_freq is None:
            frequency_table[chr] = 1
        else:
            frequency_table[chr] = cur_freq + 1

Table("Maka")