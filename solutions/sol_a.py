def solve(data, query):
    answer = []
    for name, args in query:
        count = 0
        if name in data:
            if len(args) in data[name]:
                for value in data[name][len(args)]:
                    count += check(args, value)
        answer.append(count)
    for a in answer:
        print(a)


def check(args, values):
    variables = dict()
    for arg, val in zip(args, values):
        if arg == '_':
            continue
        elif arg.startswith('_'):
            if arg in variables:
                if variables[arg] != val:
                    return 0
            else:
                variables[arg] = val
        elif arg != val:
            return 0
    return 1


def main():
    data = dict()
    line = input()
    facts = []
    while line != '':
        prev = 0
        for i, c in enumerate(line):
            if c == ')':
                facts.append(line[prev:i+1])
                prev = i+1
        line = input()
    facts = [s.strip() for s in facts]
    for f in facts:
        name, args = refine(f)
        if name in data:
            if len(args) in data[name]:
                data[name][len(args)].append(args)
            else:
                data[name][len(args)] = [args]
        else:
            data[name] = {
                len(args): [args]
            }

    query = []
    # print(data)
    line = input()
    while line != '':
        line = line.strip()
        name, args = refine(line)
        query.append((name, args))
        try:
            line = input()
        except:
            break
    # print(query)
    solve(data, query)


def refine(f):
    name = f[0:f.find('(')].strip()
    args = f[f.find('(') + 1:f.find(')')]
    args = args.split(',')
    args = [arg.strip() for arg in args]
    return name, args


if __name__ == '__main__':
    main()

