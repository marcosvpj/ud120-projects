#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []

    ### your code goes here
    # print (predictions)
    for i, item in enumerate(predictions):
        # print('Age {} net worth {} prediction {}'.format(ages[i], net_worths[i], item))
        cleaned_data.append((ages[i], net_worths[i], abs(net_worths[i] - item)))

    cleaned_data = sorted(cleaned_data, key=lambda item: item[2])

    number_of_items_to_keep = len(cleaned_data) * .9
    return cleaned_data[:81]

