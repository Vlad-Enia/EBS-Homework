import json

if __name__ == '__main__':
    with open('config.json') as config_file:
        config = json.load(config_file)

    with open('results.json') as config_file:
        results = json.load(config_file)

    for constraint in config['constraints']:
        if constraint['type'] == 'frequency':
            counter = 0
            total = 0

            for sub in results['subscriptions']:
                if constraint['field'] in sub:
                    counter += 1
                total += 1

            op = constraint['percent'][:1]

            if op == '<':
                if int((counter / total) * 100) >= int(constraint['percent'][1:]):
                    print(f"Mismatch {constraint['percent'][1:]} with {int((counter / total) * 100)} for field {constraint['field']}")
            elif op == '>':
                if int((counter / total) * 100) <= int(constraint['percent'][1:]):
                    print(f"Mismatch {constraint['percent'][1:]} with {int((counter / total) * 100)} for field {constraint['field']}")
            elif op == '=':
                if int((counter / total) * 100) != int(constraint['percent'][1:]):
                    print(f"Mismatch {constraint['percent'][1:]} with {int((counter / total) * 100)} for field {constraint['field']}")
        else:
            # Operator

            counter = 0
            total = 0

            for sub in results['subscriptions']:
                if constraint['field'] in sub:
                    if sub[constraint['field']]['operator'] == constraint['operator']:
                        counter += 1
                    total += 1

            op = constraint['percent'][:1]

            if op == '<':
                if int((counter / total) * 100) >= int(constraint['percent'][1:]):
                    print(f"Mismatch {constraint['percent'][1:]} with {int((counter / total) * 100)} for field {constraint['field']}")
            elif op == '>':
                if int((counter / total) * 100) <= int(constraint['percent'][1:]):
                    print(f"Mismatch {constraint['percent'][1:]} with {int((counter / total) * 100)} for field {constraint['field']}")
            elif op == '=':
                if int((counter / total) * 100) != int(constraint['percent'][1:]):
                    print(f"Mismatch {constraint['percent'][1:]} with {int((counter / total) * 100)} for field {constraint['field']}")
            