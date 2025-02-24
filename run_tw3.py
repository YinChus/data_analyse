import tw3_utils
import tw3_manual

DATA = 'pokemon_box.csv'


def part0():
    """
    使用第2部分中的函数计算关于Pokemon数据集的各种统计信息.
    """
    print('=== Starting Part 1 ===')
    data = tw3_utils.parse(DATA)

    print('种类数目:', tw3_manual.species_count(data))
    print('最高等级的pokemon:', tw3_manual.max_level(data))
    print('低等级的Pokemon', tw3_manual.filter_range(data, 1, 9))
    print('火系平均攻击',
          tw3_manual.mean_attack_for_type(data, 'fire'))
    print('各Pokemon种类计数:')
    print(tw3_manual.count_types(data))
    print('各Pokemon种类的最高阶')
    print(tw3_manual.highest_stage_per_type(data))
    print('各Pokemon种类的平均攻击')
    print(tw3_manual.mean_attack_per_type(data))


def main():
    part0()
    print()
    print()
    part1()
	#这里是小组作业第四部分的内容
	#在这里加入你的测试函数们


if __name__ == '__main__':
    main()
