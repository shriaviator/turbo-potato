def mask_list(df, maskname):
    """
    -[] edge cases all and none 


    Args:
        df (_type_): _description_
        maskname (_type_): _description_

    Returns:
        _type_: _description_
    """
    tempdf = df.copy(deep=True)
    final_list = []
    for loc, xray in enumerate(tempdf['name'].tolist()):
        if xray in maskname:
            final_list.append(xray)
        else:
            final_list.append("i" + str(loc))

    tempdf['name'] = final_list
    mask = tempdf.name.apply(lambda x: any(
        item for item in maskname if item == x))
    tempdf['status'] = mask
    return tempdf
