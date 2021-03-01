def solve(icpc, outside):
    icpc_name = set()
    icpc_email = set()
    for first, last, email in icpc:
        icpc_name.add(f'{first.lower()}${last.lower()}')
        icpc_email.add(email.lower())

    out_name = set()
    out_email = set()
    for first, last, email in outside:
        out_name.add(f'{first.lower()}${last.lower()}')
        out_email.add(email.lower())

    answer = []
    for first, last, email in icpc:
        if not (f'{first.lower()}${last.lower()}' in out_name or email.lower() in out_email):
            answer.append(f'I {email} {last} {first}')

    for first, last, email in outside:
        if not (f'{first.lower()}${last.lower()}' in icpc_name or email.lower() in icpc_email):
            answer.append(f'O {email} {last} {first}')

    if len(answer) == 0:
        print('No mismatches.')
    else:
        output = []
        for a in answer:
            output.append((a.lower(), a))
        output.sort()
        for _, a in output:
            print(a)


# def lower(s):
#     return s.lower()


def main():
    icpc = []
    line = input()
    while line != '':
        # icpc.append(list(map(lower, line.split())))
        icpc.append(line.split())
        line = input()

    outside = []
    line = input()
    while line != '':
        # outside.append(list(map(lower, line.split())))
        outside.append(line.split())
        try:
            line = input()
        except:
            break

    solve(icpc, outside)


if __name__ == '__main__':
    main()

