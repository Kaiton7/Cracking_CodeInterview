def rotate(M):
    n = len(M)
    for layer in range(n//2):
        first,last = layer, n-layer-1
        for i in range(first,last):
            top = M[layer][i]
            M[layer][i] = M[-i-1][layer]
            M[-i-1][layer]=M[-layer-1][-i-1]
            M[-layer-1][-i-1]=M[i][-layer-1]
            M[i][-layer-1]=top

    return M


