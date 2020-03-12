import matplotlib.pyplot as plt

def draw_graph(x, y):
    plt.plot(x, y, marker = 'o')
    plt.xlabel('BPM')
    plt.ylabel('Estimated Time in Minutes')
    plt.title('Time to one mile at BPM (assuming 3ft stride)')
    plt.show()

def generate_F_r():
    r = range(10, 170, 10)
    F = []


    for bpm in r:
        time = 5280 / (bpm * 3)
        F.append(time)

    draw_graph(r, F)

if __name__=='__main__':
    generate_F_r()
    
