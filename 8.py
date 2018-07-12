large_number = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450

large_number_array = list(map(int, str(large_number)))


def find_max_product(window_size):
    i = skip_zeros(0, window_size)
    max_product = count_initial_product(i, window_size)

    i += window_size
    window_product = max_product
    while i + window_size <= len(large_number_array):
        next_item = large_number_array[i]
        previous_item = large_number_array[i - window_size]
        if next_item is not 0:
            window_product = window_product // previous_item * next_item
            i += 1
        else:
            i = skip_zeros(i, window_size)

            if i + window_size <= len(large_number_array):
                window_product = count_initial_product(i, window_size)
            else:
                break
            i += window_size
        max_product = max(window_product, max_product)
    return max_product


def skip_zeros(i, window_size):
    while 0 in large_number_array[i:i + window_size]:
        zero_index = large_number_array[i:i + window_size].index(0)
        i += zero_index + 1
    return i


def count_initial_product(i, window_size):
    window_product = 1
    for j in range(i, i + window_size):
        window_product *= large_number_array[j]
    return window_product


assert find_max_product(4) == 5832
print(find_max_product(13))
