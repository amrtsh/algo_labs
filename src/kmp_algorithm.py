def kmp_search(haystack, needle):
    N = len(haystack)
    M = len(needle)

    lps = [0] * M
    n, m = 0, 0

    find_lps(needle, M, lps)

    indices = []

    while (N - n) >= (M - m):
        if needle[m] == haystack[n]:
            n += 1
            m += 1

        if m == M:
            start = n - m
            end = start + len(lps) - 1
            indices.append((start, end))
            m = lps[m - 1]

        elif n < N and needle[m] != haystack[n]:
            if m != 0:
                m = lps[m - 1]
            else:
                n += 1

    return indices


def find_lps(needle, M, lps):
    lps[0] = 0
    j, i = 0, 1

    while i < M:
        if needle[i] == needle[j]:
            j += 1
            lps[i] = j
            i += 1
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                lps[i] = 0
                i += 1


if __name__ == '__main__':
    haystack = input("Enter haystack: ")
    needle = input("Enter needle: ")
    # haystack = "AABAACAADAABAABA"
    # needle = "AABA"
    result = kmp_search(haystack, needle)
    print(f"Needle at indices: {result}")
