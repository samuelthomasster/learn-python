def get_larges_numbers(numbers, n):
    numbers.sort()
    return numbers[-4:]


if __name__ == "__main__":
    nums = [1,4,4,2,896,223,457,235,363,1]

    print(nums)

    nums_sorted = get_larges_numbers(nums, len(nums))

    print(f'Sorted numbers: {nums_sorted}')

    print(f'After sorting {nums}')