from urllib.request import urlopen

with open("../data/speed-dating.csv", "w") as output_file:
    data_found = False
    attributes = []
    for line in urlopen("https://www.openml.org/data/download/13153954/speeddating.arff"):
        decoded_line = line.decode('UTF-8').strip()
        if '@attribute' in decoded_line:
            end_od_attribute_name = len(decoded_line)
            if 'numeric' in decoded_line:
                end_od_attribute_name = decoded_line.index('numeric') - 1
            elif '{' in decoded_line:
                end_od_attribute_name = decoded_line.index('{') - 1

            attributes.append(decoded_line[len('@attribute'): end_od_attribute_name].replace('\'', '').strip())
        if data_found:
            # decoded_line = decoded_line.replace("yes", "true")
            # decoded_line = decoded_line.replace("no", "false")
            decoded_line = decoded_line.replace("?", "")
            output_file.write(decoded_line.lower() + '\n')

        if decoded_line == "@data":
            output_file.write(','.join(attributes).lower() + '\n')
            data_found = True

    output_file.close()
