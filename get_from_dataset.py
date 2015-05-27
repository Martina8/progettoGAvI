
def get_sentence_from_dataset(dataset):
    """
    Questa funzione ritorna una lista di
    :param dataset:
    :return: lista di frasi del dataset
    """
    with open (dataset, "r") as myfile:
        dataset = myfile.readlines()

    data = []
    for d in dataset:
        d = ''.join(d.splitlines())
        data.append(d)

    return data