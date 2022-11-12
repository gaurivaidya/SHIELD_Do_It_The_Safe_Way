import matplotlib
import pandas as pd
from os import path, pathsep
import numpy as np

# from utilities.stats.trackers import first_pareto_list
# from utilities.stats import trackers

matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rc('font', family='Arial')


def save_pareto_fitness_plot():
    """
    Saves a plot of the current fitness for a pareto front.

    :return: Nothing
    """

    # from algorithm.parameters import params

    # Initialise up figure instance.
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)
    # if stats['gen']==0:
    #     print(first_pareto_list)
    # elif 
    # first_pareto_list = [[[0.22725955138659062, 0.5477965358158541], [4.732401260207763, 4.384547042986675]],[[0.7312813650176687, 0.7652549396876758], [3.6079861774750834, 3.126361521721867]]]
    # first_pareto_list = [[[[[7.695920866809072, 7.80359414626648], [264, 258]], [[7.695920866809072, 7.80359414626648, 7.80359414626648], [264, 258, 258]], [[7.80359414626648, 7.80359414626648, 7.80359414626648], [258, 258, 258]], [[7.80359414626648, 7.80359414626648, 7.80359414626648], [258, 258, 258]], [[7.80359414626648, 7.80359414626648, 7.80359414626648], [258, 258, 258]], [[7.80359414626648, 7.80359414626648, 7.80359414626648], [258, 258, 258]]]], [[[[7.671809453662047, 7.693769172252499, 7.816606967168758], [263, 262, 255]], [[7.671809453662047, 7.693769172252499, 7.816606967168758], [263, 262, 255]], [[7.671809453662047, 7.693769172252499, 7.827766918471131], [263, 262, 256]], [[7.671809453662047, 7.671809453662047, 7.693769172252499], [263, 263, 262]], [[7.671809453662047, 7.671809453662047, 7.671809453662047], [263, 263, 263]], [[7.671809453662047, 7.671809453662047, 7.671809453662047], [263, 263, 263]]]]]        # Set up the figure.
    # this is entropy and hamming distance
#     first_pareto_list = [[[[[7.685389828016366, 7.7895341627831645], [252, 250]], [[7.685389828016366, 7.685389828016366, 7.7895341627831645], [252, 252, 250]], [[7.687134651213254, 7.7895341627831645, 7.7895341627831645], [256, 250, 250]], [[7.795537524438149], [258]], [[7.795537524438149], [258]], [[7.795537524438149, 7.795537524438149], [258, 258]]]],
# [[[[7.775828041596479], [275]], [[7.775828041596479], [275]], [[7.775828041596479, 7.813413622470004], [275, 273]], [[7.775828041596479, 7.813413622470004, 7.813413622470004], [275, 273, 273]], [[7.813413622470004, 7.813413622470004, 7.813413622470004], [273, 273, 273]], [[7.813413622470004, 7.813413622470004, 7.813413622470004], [273, 273, 273]]]],
# [[[[7.784542525925181], [263]], [[7.784542525925181], [263]], [[7.784542525925181, 7.784542525925181], [263, 263]], [[7.784542525925181, 7.784542525925181, 7.801265105331704], [263, 263, 256]], [[7.784542525925181, 7.784542525925181, 7.801265105331704], [263, 263, 256]], [[7.784542525925181, 7.784542525925181, 7.801265105331704], [263, 263, 256]]]],
# [[[[7.664970403204613, 7.76695002855184, 7.7703728881032], [265, 260, 234]], [[7.664970403204613, 7.76695002855184, 7.7703728881032], [265, 260, 234]], [[7.711688390727222, 7.76695002855184, 7.7703728881032], [265, 260, 234]], [[7.711688390727222, 7.711688390727222, 7.76695002855184], [265, 265, 260]], [[7.711688390727222, 7.711688390727222, 7.76695002855184], [265, 265, 260]], [[7.711688390727222, 7.711688390727222, 7.76695002855184], [265, 265, 260]]]],
# [[[[7.660627814810879, 7.660755437674314, 7.737470417015613, 7.788064285316425], [256, 250, 243, 235]], [[7.660627814810879, 7.660755437674314, 7.775538108435375], [256, 250, 243]], [[7.660627814810879, 7.660755437674314, 7.775538108435375], [256, 250, 243]], [[7.660627814810879, 7.660755437674314, 7.775538108435375], [256, 250, 243]], [[7.660627814810879, 7.660755437674314, 7.775538108435375], [256, 250, 243]], [[7.660755437674314, 7.775538108435375, 7.775538108435375], [250, 243, 243]]]],
# [[[[7.686078601237068, 7.751567994413617], [260, 252]], [[7.686078601237068, 7.751567994413617, 7.751567994413617], [260, 252, 252]], [[7.686078601237068, 7.722369659352703, 7.751567994413617], [260, 255, 252]], [[7.722369659352703, 7.751567994413617, 7.751567994413617], [255, 252, 252]], [[7.722369659352703, 7.751567994413617, 7.751567994413617], [255, 252, 252]], [[7.722369659352703, 7.751567994413617, 7.751567994413617], [255, 252, 252]]]],
# [[[[7.746170091588927, 7.801067262128946, 7.810792916611545, 7.82786276251271], [268, 262, 252, 226]], [[7.801067262128946, 7.810792916611545, 7.82786276251271], [262, 252, 226]], [[7.813942467444823, 7.82786276251271, 7.82786276251271], [274, 226, 226]], [[7.813942467444823, 7.82786276251271, 7.82786276251271], [274, 226, 226]], [[7.813942467444823, 7.828580443260211], [274, 250]], [[7.823391599827923, 7.828580443260211], [276, 250]]]],
# [[[[7.7076055219999455, 7.756410056182883, 7.793834247049209], [268, 266, 255]], [[7.7076055219999455, 7.787189501340444, 7.793834247049209], [268, 267, 255]], [[7.7076055219999455, 7.787189501340444, 7.793834247049209], [268, 267, 255]], [[7.7076055219999455, 7.787189501340444, 7.793834247049209], [268, 267, 255]], [[7.787189501340444, 7.793834247049209, 7.812007269655537], [267, 255, 248]], [[7.787189501340444, 7.793834247049209, 7.812007269655537], [267, 255, 248]]]],
# [[[[7.751323171595375, 7.788135900352104, 7.800444620149048], [267, 254, 249]], [[7.751323171595375, 7.788135900352104, 7.800444620149048], [267, 254, 249]], [[7.771638782779274, 7.788135900352104, 7.800444620149048], [266, 254, 249]], [[7.771638782779274, 7.788135900352104, 7.800444620149048], [266, 254, 249]], [[7.788135900352104, 7.800444620149048, 7.800444620149048], [254, 249, 249]], [[7.78568317197478, 7.788135900352104, 7.788135900352104], [260, 254, 254]]]],
# [[[[7.798341578627121], [263]], [[7.798341578627121, 7.798341578627121], [263, 263]], [[7.798341578627121, 7.798341578627121, 7.805529519781149], [263, 263, 260]], [[7.795448589531756, 7.798341578627121, 7.798341578627121], [266, 263, 263]], [[7.795448589531756, 7.798341578627121, 7.798341578627121], [266, 263, 263]], [[7.798341578627121, 7.798341578627121, 7.810937858124849], [263, 263, 251]]]],
# [[[[7.764163824549517, 7.852960604483878], [264, 261]], [[7.764163824549517, 7.764163824549517, 7.852960604483878], [264, 264, 261]], [[7.764163824549517, 7.764163824549517, 7.852960604483878], [264, 264, 261]], [[7.764163824549517, 7.764163824549517, 7.764163824549517], [264, 264, 264]], [[7.764163824549517, 7.764163824549517, 7.764163824549517], [264, 264, 264]], [[7.764163824549517, 7.764163824549517, 7.764163824549517], [264, 264, 264]]]],
# [[[[7.619261473022725, 7.804635729264251], [263, 253]], [[7.619261473022725, 7.619261473022725, 7.804635729264251], [263, 263, 253]], [[7.619261473022725, 7.619261473022725, 7.619261473022725], [263, 263, 263]], [[7.619261473022725, 7.619261473022725, 7.656539610169068], [263, 263, 260]], [[7.619261473022725, 7.619261473022725, 7.619261473022725], [263, 263, 263]], [[7.619261473022725, 7.619261473022725, 7.619261473022725], [263, 263, 263]]]],
# [[[[7.7420994982541504, 7.795914545536054, 7.800749205451831, 7.827974111510932], [264, 259, 251, 244]], [[7.795914545536054, 7.800749205451831, 7.827974111510932], [259, 251, 244]], [[7.795914545536054, 7.795914545536054, 7.800749205451831], [259, 259, 251]], [[7.694263622053462, 7.795914545536054, 7.795914545536054], [261, 259, 259]], [[7.694263622053462, 7.795914545536054, 7.795914545536054], [261, 259, 259]], [[7.694263622053462, 7.795914545536054, 7.795914545536054], [261, 259, 259]]]],
# [[[[7.775212188478947, 7.7881560095046005], [271, 250]], [[7.7881560095046005, 7.7881560095046005, 7.7881560095046005], [250, 250, 250]], [[7.778103012502159, 7.7881560095046005, 7.7881560095046005], [269, 250, 250]], [[7.784915609672488, 7.7881560095046005, 7.7881560095046005], [275, 250, 250]], [[7.784915609672488, 7.7881560095046005, 7.7881560095046005], [275, 250, 250]], [[7.784915609672488, 7.784915609672488, 7.7881560095046005], [275, 275, 250]]]],
# [[[[7.747714602602863, 7.762183324119359], [268, 255]], [[7.747714602602863, 7.762183324119359, 7.762183324119359], [268, 255, 255]], [[7.747714602602863, 7.751366947307293, 7.762183324119359], [268, 267, 255]], [[7.751366947307293, 7.762183324119359, 7.763620997876491], [267, 255, 243]], [[7.751366947307293, 7.762183324119359, 7.763620997876491], [267, 255, 243]], [[7.751366947307293, 7.751366947307293, 7.762183324119359], [267, 267, 255]]]],
# [[[[7.770217977329326], [256]], [[7.770217977329326, 7.770217977329326, 7.770217977329326], [256, 256, 256]], [[7.770217977329326, 7.770217977329326, 7.770217977329326], [256, 256, 256]], [[7.769522336307862, 7.770217977329326, 7.770217977329326], [261, 256, 256]], [[7.755549954941858, 7.769522336307862, 7.770217977329326], [284, 261, 256]], [[7.769522336307862, 7.770217977329326, 7.770217977329326], [261, 256, 256]]]],
# [[[[7.743173695516147], [259]], [[7.699566875010865, 7.743173695516147, 7.745479092488615], [265, 259, 247]], [[7.743173695516147, 7.745479092488615, 7.745479092488615], [259, 247, 247]], [[7.743173695516147, 7.7618102418068995, 7.766146630904541], [259, 251, 247]], [[7.743173695516147, 7.7618102418068995, 7.766146630904541], [259, 251, 247]], [[7.743173695516147, 7.743173695516147, 7.7618102418068995], [259, 259, 251]]]],
# [[[[7.784444373875594, 7.837923885137446], [262, 256]], [[7.784444373875594, 7.784444373875594, 7.837923885137446], [262, 262, 256]], [[7.784444373875594, 7.784444373875594, 7.837923885137446], [262, 262, 256]], [[7.784444373875594, 7.784444373875594, 7.837923885137446], [262, 262, 256]], [[7.784444373875594, 7.784444373875594, 7.837923885137446], [262, 262, 256]], [[7.784444373875594, 7.784444373875594, 7.784444373875594], [262, 262, 262]]]],
# [[[[7.731542022389258, 7.732254599980654, 7.745542632240783, 7.843471592717151], [249, 248, 244, 220]], [[7.754090921005205, 7.843471592717151, 7.843471592717151], [261, 220, 220]], [[7.772861728659693, 7.8265669377119576, 7.843471592717151], [263, 262, 220]], [[7.772861728659693, 7.8265669377119576, 7.843471592717151], [263, 262, 220]], [[7.8265669377119576, 7.843471592717151, 7.843471592717151], [262, 220, 220]], [[7.8265669377119576, 7.843471592717151, 7.843471592717151], [262, 220, 220]]]],
# [[[[7.692874601582938, 7.827087923748134], [274, 269]], [[7.692874601582938, 7.827087923748134, 7.827087923748134], [274, 269, 269]], [[7.692874601582938, 7.827087923748134, 7.827087923748134], [274, 269, 269]], [[7.827087923748134, 7.827087923748134, 7.827087923748134], [269, 269, 269]], [[7.827087923748134, 7.827087923748134, 7.827087923748134], [269, 269, 269]], [[7.827087923748134, 7.827087923748134, 7.827087923748134], [269, 269, 269]]]],
# [[[[7.7018794802130035, 7.728694877615614, 7.747936690460449], [257, 253, 251]], [[7.7018794802130035, 7.728694877615614, 7.747936690460449], [257, 253, 251]], [[7.728694877615614, 7.747936690460449, 7.747936690460449], [253, 251, 251]], [[7.750440422177604], [256]], [[7.750440422177604, 7.750440422177604, 7.750440422177604], [256, 256, 256]], [[7.750440422177604, 7.750440422177604, 7.750440422177604], [256, 256, 256]]]],
# [[[[7.673637607281727, 7.696596866506111, 7.768726648786996, 7.771366138287942], [277, 254, 247, 240]], [[7.673637607281727, 7.673637607281727, 7.782376804653239], [277, 277, 267]], [[7.673637607281727, 7.673637607281727, 7.673637607281727], [277, 277, 277]], [[7.673637607281727, 7.673637607281727, 7.673637607281727], [277, 277, 277]], [[7.673637607281727, 7.673637607281727, 7.673637607281727], [277, 277, 277]], [[7.673637607281727, 7.673637607281727, 7.673637607281727], [277, 277, 277]]]],
# [[[[7.674466531229254, 7.7914408966863995, 7.826900507186182], [264, 246, 241]], [[7.7914408966863995, 7.7914408966863995, 7.7914408966863995], [246, 246, 246]], [[7.7914408966863995, 7.7914408966863995, 7.7914408966863995], [246, 246, 246]], [[7.794041385491365], [251]], [[7.699844569613434, 7.794041385491365], [260, 251]], [[7.699844569613434, 7.699844569613434, 7.699844569613434], [260, 260, 260]]]],
# [[[[7.659208318219174, 7.7770257542623, 7.807667025172552], [261, 251, 241]], [[7.659208318219174, 7.7770257542623, 7.807667025172552], [261, 251, 241]], [[7.659208318219174, 7.7770257542623, 7.786452673373048], [261, 251, 250]], [[7.680112206954409, 7.7770257542623, 7.786452673373048], [276, 251, 250]], [[7.680112206954409, 7.680112206954409, 7.7770257542623], [276, 276, 251]], [[7.680112206954409, 7.680112206954409, 7.680112206954409], [276, 276, 276]]]],
# [[[[7.8413742231816155], [271]], [[7.8413742231816155], [271]], [[7.8413742231816155, 7.8413742231816155, 7.8413742231816155], [271, 271, 271]], [[7.8413742231816155, 7.8413742231816155, 7.8413742231816155], [271, 271, 271]], [[7.8413742231816155, 7.8413742231816155, 7.8413742231816155], [271, 271, 271]], [[7.8413742231816155, 7.8413742231816155, 7.8413742231816155], [271, 271, 271]]]],
# [[[[7.760918348729415], [263]], [[7.760918348729415], [263]], [[7.760918348729415, 7.760918348729415, 7.760918348729415], [263, 263, 263]], [[7.760918348729415, 7.760918348729415, 7.760918348729415], [263, 263, 263]], [[7.760918348729415, 7.760918348729415, 7.765398167116907], [263, 263, 249]], [[7.760918348729415, 7.760918348729415, 7.765398167116907], [263, 263, 249]]]],
# [[[[7.751552042747149, 7.777628291532922], [256, 243]], [[7.751552042747149, 7.751552042747149, 7.777628291532922], [256, 256, 243]], [[7.751552042747149, 7.751552042747149, 7.751552042747149], [256, 256, 256]], [[7.751552042747149, 7.751552042747149, 7.751552042747149], [256, 256, 256]], [[7.751552042747149, 7.751552042747149, 7.751552042747149], [256, 256, 256]], [[7.751552042747149, 7.751552042747149, 7.751552042747149], [256, 256, 256]]]],
# [[[[7.761046987340121, 7.775879615977619, 7.795121379559701], [262, 251, 239]], [[7.761046987340121, 7.775879615977619, 7.775879615977619], [262, 251, 251]], [[7.775879615977619, 7.775879615977619, 7.775879615977619], [251, 251, 251]], [[7.775879615977619, 7.775879615977619, 7.775879615977619], [251, 251, 251]], [[7.765471235251798, 7.793539033411209], [271, 270]], [[7.765471235251798, 7.765471235251798, 7.793539033411209], [271, 271, 270]]]],
# [[[[7.732846800204113, 7.796675910887029], [278, 264]], [[7.78927885628895, 7.796675910887029, 7.796675910887029], [279, 264, 264]], [[7.78927885628895, 7.796675910887029, 7.796675910887029], [279, 264, 264]], [[7.78927885628895, 7.796675910887029, 7.796675910887029], [279, 264, 264]], [[7.78927885628895, 7.78927885628895, 7.796675910887029], [279, 279, 264]], [[7.78927885628895, 7.796675910887029, 7.824637613311041], [279, 264, 236]]]],
# [[[[7.776732047002645, 7.789250365560948], [258, 246]], [[7.804998057993818], [277]], [[7.804998057993818, 7.804998057993818, 7.804998057993818], [277, 277, 277]], [[7.804998057993818, 7.804998057993818, 7.812683341060344], [277, 277, 265]], [[7.804998057993818, 7.804998057993818, 7.804998057993818], [277, 277, 277]], [[7.804998057993818, 7.804998057993818, 7.804998057993818], [277, 277, 277]]]]]
# this is entropy and autocorr
    first_pareto_list = [[[[[7.73070019142518, 7.762967077433799], [0.0706329345703125, 0.072021484375]], [[7.73070019142518, 7.762967077433799, 7.762967077433799], [0.0706329345703125, 0.072021484375, 0.072021484375]], [[7.762967077433799, 7.762967077433799, 7.785622132685267], [0.072021484375, 0.072021484375, 0.075347900390625]], [[7.762967077433799, 7.785622132685267, 7.791623299026465], [0.072021484375, 0.075347900390625, 0.1187286376953125]], [[7.762967077433799, 7.796573597739523], [0.072021484375, 0.072540283203125]], [[7.762967077433799, 7.796573597739523, 7.796573597739523], [0.072021484375, 0.072540283203125, 0.072540283203125]]]],
[[[[7.774073729446838], [0.072662353515625]], [[7.774073729446838, 7.774073729446838], [0.072662353515625, 0.072662353515625]], [[7.788984262062313, 7.793923289396625], [0.069244384765625, 0.0797271728515625]], [[7.788984262062313, 7.788984262062313, 7.793923289396625], [0.069244384765625, 0.069244384765625, 0.0797271728515625]], [[7.788984262062313, 7.788984262062313, 7.788984262062313], [0.069244384765625, 0.069244384765625, 0.069244384765625]], [[7.788984262062313, 7.788984262062313, 7.788984262062313], [0.069244384765625, 0.069244384765625, 0.069244384765625]]]],
[[[[7.6225845946046205, 7.70031548732198, 7.804381263969192], [0.0702972412109375, 0.074859619140625, 0.079345703125]], [[7.70031548732198, 7.804381263969192, 7.818715872151196], [0.074859619140625, 0.079345703125, 0.0830078125]], [[7.70031548732198, 7.70031548732198, 7.804381263969192], [0.074859619140625, 0.074859619140625, 0.079345703125]], [[7.70031548732198, 7.70031548732198, 7.804381263969192], [0.074859619140625, 0.074859619140625, 0.079345703125]], [[7.714692145417734, 7.804381263969192], [0.072662353515625, 0.079345703125]], [[7.714692145417734, 7.825870660044241], [0.072662353515625, 0.07867431640625]]]],
[[[[7.741323972669735, 7.7741283062969035, 7.820741242080141], [0.069366455078125, 0.0713348388671875, 0.111297607421875]], [[7.741323972669735, 7.741323972669735, 7.7741283062969035], [0.069366455078125, 0.069366455078125, 0.0713348388671875]], [[7.741323972669735, 7.741323972669735, 7.7741283062969035], [0.069366455078125, 0.069366455078125, 0.0713348388671875]], [[7.741323972669735, 7.741323972669735, 7.741323972669735], [0.069366455078125, 0.069366455078125, 0.069366455078125]], [[7.741323972669735, 7.741323972669735, 7.741323972669735], [0.069366455078125, 0.069366455078125, 0.069366455078125]], [[7.741323972669735, 7.741323972669735, 7.741323972669735], [0.069366455078125, 0.069366455078125, 0.069366455078125]]]],
[[[[7.8437177128497115], [0.06494140625]], [[7.8437177128497115], [0.06494140625]], [[7.8437177128497115, 7.8437177128497115, 7.8437177128497115], [0.06494140625, 0.06494140625, 0.06494140625]], [[7.8437177128497115, 7.8437177128497115, 7.8437177128497115], [0.06494140625, 0.06494140625, 0.06494140625]], [[7.8437177128497115, 7.8437177128497115, 7.8437177128497115], [0.06494140625, 0.06494140625, 0.06494140625]], [[7.8437177128497115, 7.8437177128497115, 7.8437177128497115], [0.06494140625, 0.06494140625, 0.06494140625]]]],
[[[[7.745516658200765, 7.75815213741701, 7.769162674620569], [0.0691375732421875, 0.075225830078125, 0.083038330078125]], [[7.745516658200765, 7.75815213741701, 7.769162674620569], [0.0691375732421875, 0.075225830078125, 0.083038330078125]], [[7.745516658200765, 7.745516658200765, 7.75815213741701], [0.0691375732421875, 0.0691375732421875, 0.075225830078125]], [[7.745516658200765, 7.745516658200765, 7.745516658200765], [0.0691375732421875, 0.0691375732421875, 0.0691375732421875]], [[7.745516658200765, 7.745516658200765, 7.745516658200765], [0.0691375732421875, 0.0691375732421875, 0.0691375732421875]], [[7.745516658200765, 7.745516658200765, 7.745516658200765], [0.0691375732421875, 0.0691375732421875, 0.0691375732421875]]]],
[[[[7.74599465369781, 7.77971300509974], [0.0667877197265625, 0.0770263671875]], [[7.762449837726958, 7.77971300509974], [0.062652587890625, 0.0770263671875]], [[7.762449837726958, 7.762449837726958, 7.77971300509974], [0.062652587890625, 0.062652587890625, 0.0770263671875]], [[7.762449837726958, 7.762449837726958, 7.762449837726958], [0.062652587890625, 0.062652587890625, 0.062652587890625]], [[7.762449837726958, 7.762449837726958, 7.762449837726958], [0.062652587890625, 0.062652587890625, 0.062652587890625]], [[7.762449837726958, 7.762449837726958, 7.762449837726958], [0.062652587890625, 0.062652587890625, 0.062652587890625]]]],
[[[[7.739635697299359, 7.7896309496046445, 7.805798865859231], [0.06939697265625, 0.076141357421875, 0.0763092041015625]], [[7.739635697299359, 7.832143421674621], [0.06939697265625, 0.0752410888671875]], [[7.739635697299359, 7.832143421674621, 7.832143421674621], [0.06939697265625, 0.0752410888671875, 0.0752410888671875]], [[7.739635697299359, 7.832143421674621, 7.832143421674621], [0.06939697265625, 0.0752410888671875, 0.0752410888671875]], [[7.739635697299359, 7.801385778199231, 7.832143421674621], [0.06939697265625, 0.071807861328125, 0.0752410888671875]], [[7.829104004722395, 7.832143421674621, 7.832143421674621], [0.064117431640625, 0.0752410888671875, 0.0752410888671875]]]],
[[[[7.774317817790871, 7.788244169769362], [0.0675201416015625, 0.0742645263671875]], [[7.774317817790871, 7.774317817790871, 7.788244169769362], [0.0675201416015625, 0.0675201416015625, 0.0742645263671875]], [[7.774317817790871, 7.774317817790871, 7.774317817790871], [0.0675201416015625, 0.0675201416015625, 0.0675201416015625]], [[7.774317817790871, 7.774317817790871, 7.774317817790871], [0.0675201416015625, 0.0675201416015625, 0.0675201416015625]], [[7.774317817790871, 7.774317817790871, 7.774317817790871], [0.0675201416015625, 0.0675201416015625, 0.0675201416015625]], [[7.774317817790871, 7.774317817790871, 7.774317817790871], [0.0675201416015625, 0.0675201416015625, 0.0675201416015625]]]],
[[[[7.742584355435917, 7.756535621944374, 7.762434217393606, 7.833413748976135], [0.06951904296875, 0.0731658935546875, 0.080902099609375, 0.111602783203125]], [[7.756535621944374, 7.762434217393606, 7.762434217393606], [0.0731658935546875, 0.080902099609375, 0.080902099609375]], [[7.756535621944374, 7.762434217393606, 7.762434217393606], [0.0731658935546875, 0.080902099609375, 0.080902099609375]], [[7.756535621944374, 7.762434217393606, 7.762434217393606], [0.0731658935546875, 0.080902099609375, 0.080902099609375]], [[7.756535621944374, 7.762434217393606, 7.762434217393606], [0.0731658935546875, 0.080902099609375, 0.080902099609375]], [[7.756535621944374, 7.762434217393606, 7.762434217393606], [0.0731658935546875, 0.080902099609375, 0.080902099609375]]]],
[[[[7.816908235817721, 7.82366507664852], [0.0734100341796875, 0.076629638671875]], [[7.82366507664852, 7.82366507664852, 7.82366507664852], [0.076629638671875, 0.076629638671875, 0.076629638671875]], [[7.82366507664852, 7.82366507664852, 7.82366507664852], [0.076629638671875, 0.076629638671875, 0.076629638671875]], [[7.819624028441723, 7.82366507664852, 7.82366507664852], [0.067840576171875, 0.076629638671875, 0.076629638671875]], [[7.82366507664852, 7.82366507664852, 7.82366507664852], [0.076629638671875, 0.076629638671875, 0.076629638671875]], [[7.82366507664852, 7.82366507664852, 7.839489175114506], [0.076629638671875, 0.076629638671875, 0.11712646484375]]]],
[[[[7.634197333532897, 7.79847321600671], [0.0689697265625, 0.0736083984375]], [[7.634197333532897, 7.79847321600671], [0.0689697265625, 0.0736083984375]], [[7.634197333532897, 7.634197333532897, 7.79847321600671], [0.0689697265625, 0.0689697265625, 0.0736083984375]], [[7.634197333532897, 7.634197333532897, 7.79847321600671], [0.0689697265625, 0.0689697265625, 0.0736083984375]], [[7.634197333532897, 7.634197333532897, 7.79847321600671], [0.0689697265625, 0.0689697265625, 0.0736083984375]], [[7.634197333532897, 7.634197333532897, 7.634197333532897], [0.0689697265625, 0.0689697265625, 0.0689697265625]]]],
[[[[7.6888415706100695, 7.7850625460099385], [0.066680908203125, 0.071136474609375]], [[7.6888415706100695, 7.6888415706100695, 7.7850625460099385], [0.066680908203125, 0.066680908203125, 0.071136474609375]], [[7.6888415706100695, 7.6888415706100695, 7.7850625460099385], [0.066680908203125, 0.066680908203125, 0.071136474609375]], [[7.6888415706100695, 7.7850625460099385, 7.7850625460099385], [0.066680908203125, 0.071136474609375, 0.071136474609375]], [[7.6888415706100695, 7.7850625460099385, 7.7850625460099385], [0.066680908203125, 0.071136474609375, 0.071136474609375]], [[7.6888415706100695, 7.7850625460099385, 7.7850625460099385], [0.066680908203125, 0.071136474609375, 0.071136474609375]]]],
[[[[7.781082886848202], [0.069305419921875]], [[7.781082886848202], [0.069305419921875]], [[7.781082886848202, 7.781082886848202], [0.069305419921875, 0.069305419921875]], [[7.781082886848202, 7.781082886848202, 7.781082886848202], [0.069305419921875, 0.069305419921875, 0.069305419921875]], [[7.781082886848202, 7.781082886848202, 7.781082886848202], [0.069305419921875, 0.069305419921875, 0.069305419921875]], [[7.781082886848202, 7.781082886848202, 7.781082886848202], [0.069305419921875, 0.069305419921875, 0.069305419921875]]]],
[[[[7.791283148690895], [0.0706024169921875]], [[7.791283148690895], [0.0706024169921875]], [[7.791283148690895, 7.791283148690895], [0.0706024169921875, 0.0706024169921875]], [[7.791283148690895, 7.791283148690895], [0.0706024169921875, 0.0706024169921875]], [[7.791283148690895, 7.791283148690895, 7.791283148690895], [0.0706024169921875, 0.0706024169921875, 0.0706024169921875]], [[7.791283148690895, 7.791283148690895, 7.791283148690895], [0.0706024169921875, 0.0706024169921875, 0.0706024169921875]]]],
[[[[7.764423049590857, 7.767644522461683], [0.071990966796875, 0.101593017578125]], [[7.764423049590857, 7.767644522461683, 7.767644522461683], [0.071990966796875, 0.101593017578125, 0.101593017578125]], [[7.767644522461683, 7.767644522461683, 7.767644522461683], [0.101593017578125, 0.101593017578125, 0.101593017578125]], [[7.767644522461683, 7.767644522461683, 7.767644522461683], [0.101593017578125, 0.101593017578125, 0.101593017578125]], [[7.767644522461683, 7.767644522461683, 7.767644522461683], [0.101593017578125, 0.101593017578125, 0.101593017578125]], [[7.767644522461683, 7.767644522461683, 7.767644522461683], [0.101593017578125, 0.101593017578125, 0.101593017578125]]]],
[[[[7.761118524393539, 7.786636645678613], [0.067657470703125, 0.072906494140625]], [[7.791032580625895], [0.067657470703125]], [[7.791032580625895, 7.791032580625895], [0.067657470703125, 0.067657470703125]], [[7.791032580625895, 7.791032580625895], [0.067657470703125, 0.067657470703125]], [[7.791032580625895, 7.791032580625895, 7.791032580625895], [0.067657470703125, 0.067657470703125, 0.067657470703125]], [[7.791032580625895, 7.791032580625895, 7.791032580625895], [0.067657470703125, 0.067657470703125, 0.067657470703125]]]],
[[[[7.772860620178907], [0.075836181640625]], [[7.772860620178907], [0.075836181640625]], [[7.772860620178907, 7.772860620178907], [0.075836181640625, 0.075836181640625]], [[7.772860620178907, 7.772860620178907, 7.772860620178907], [0.075836181640625, 0.075836181640625, 0.075836181640625]], [[7.772860620178907, 7.772860620178907, 7.772860620178907], [0.075836181640625, 0.075836181640625, 0.075836181640625]], [[7.772860620178907, 7.772860620178907, 7.772860620178907], [0.075836181640625, 0.075836181640625, 0.075836181640625]]]],
[[[[7.714131758667752, 7.72845281505783, 7.824256937539051], [0.073455810546875, 0.0844268798828125, 0.1083984375]], [[7.714131758667752, 7.72845281505783, 7.824256937539051], [0.073455810546875, 0.0844268798828125, 0.1083984375]], [[7.72845281505783, 7.824256937539051, 7.824256937539051], [0.0844268798828125, 0.1083984375, 0.1083984375]], [[7.824256937539051, 7.824256937539051, 7.824256937539051], [0.1083984375, 0.1083984375, 0.1083984375]], [[7.824256937539051, 7.824256937539051, 7.824256937539051], [0.1083984375, 0.1083984375, 0.1083984375]], [[7.819761083724352, 7.824256937539051, 7.824256937539051], [0.087554931640625, 0.1083984375, 0.1083984375]]]],
[[[[7.807378347155614], [0.06341552734375]], [[7.807378347155614, 7.807378347155614, 7.81116987845757], [0.06341552734375, 0.06341552734375, 0.0717620849609375]], [[7.807378347155614, 7.807378347155614, 7.81116987845757], [0.06341552734375, 0.06341552734375, 0.0717620849609375]], [[7.807378347155614, 7.807378347155614, 7.81116987845757], [0.06341552734375, 0.06341552734375, 0.0717620849609375]], [[7.807378347155614, 7.807378347155614, 7.81116987845757], [0.06341552734375, 0.06341552734375, 0.0717620849609375]], [[7.807378347155614, 7.807378347155614, 7.81116987845757], [0.06341552734375, 0.06341552734375, 0.0717620849609375]]]],
[[[[7.729406869901548, 7.7700809468610545], [0.0808258056640625, 0.1184844970703125]], [[7.728918016663097, 7.729406869901548, 7.7700809468610545], [0.0729217529296875, 0.0808258056640625, 0.1184844970703125]], [[7.729406869901548, 7.7700809468610545, 7.7700809468610545], [0.0808258056640625, 0.1184844970703125, 0.1184844970703125]], [[7.775696574703309], [0.0738525390625]], [[7.775696574703309, 7.775696574703309, 7.781888186794074], [0.0738525390625, 0.0738525390625, 0.0749053955078125]], [[7.775696574703309, 7.775696574703309, 7.775696574703309], [0.0738525390625, 0.0738525390625, 0.0738525390625]]]],
[[[[7.668332782348162, 7.676404137065321, 7.723139786489316], [0.066070556640625, 0.0751953125, 0.123565673828125]], [[7.668332782348162, 7.737962373704427], [0.066070556640625, 0.0710601806640625]], [[7.737962373704427, 7.737962373704427, 7.7568041903743365], [0.0710601806640625, 0.0710601806640625, 0.11505126953125]], [[7.737962373704427, 7.737962373704427, 7.75095462099682], [0.0710601806640625, 0.0710601806640625, 0.10760498046875]], [[7.737962373704427, 7.737962373704427, 7.75095462099682], [0.0710601806640625, 0.0710601806640625, 0.10760498046875]], [[7.737962373704427, 7.737962373704427, 7.737962373704427], [0.0710601806640625, 0.0710601806640625, 0.0710601806640625]]]],
[[[[7.659398636472183, 7.735987980214612, 7.766586751705411], [0.0694427490234375, 0.0835418701171875, 0.1114044189453125]], [[7.659398636472183, 7.659398636472183, 7.735987980214612], [0.0694427490234375, 0.0694427490234375, 0.0835418701171875]], [[7.659398636472183, 7.659398636472183, 7.735987980214612], [0.0694427490234375, 0.0694427490234375, 0.0835418701171875]], [[7.659398636472183, 7.659398636472183, 7.735987980214612], [0.0694427490234375, 0.0694427490234375, 0.0835418701171875]], [[7.659398636472183, 7.659398636472183, 7.773985398941933], [0.0694427490234375, 0.0694427490234375, 0.0702972412109375]], [[7.659398636472183, 7.659398636472183, 7.659398636472183], [0.0694427490234375, 0.0694427490234375, 0.0694427490234375]]]],
[[[[7.63483420464411, 7.745244582893058, 7.802609735417477], [0.076019287109375, 0.0948638916015625, 0.1070709228515625]], [[7.63483420464411, 7.745244582893058, 7.802609735417477], [0.076019287109375, 0.0948638916015625, 0.1070709228515625]], [[7.63483420464411, 7.63483420464411, 7.745244582893058], [0.076019287109375, 0.076019287109375, 0.0948638916015625]], [[7.63483420464411, 7.63483420464411, 7.745244582893058], [0.076019287109375, 0.076019287109375, 0.0948638916015625]], [[7.6602854053695655, 7.745244582893058], [0.067291259765625, 0.0948638916015625]], [[7.6602854053695655, 7.745244582893058, 7.745244582893058], [0.067291259765625, 0.0948638916015625, 0.0948638916015625]]]],
[[[[7.7792975485521785], [0.0699310302734375]], [[7.7792975485521785, 7.7792975485521785], [0.0699310302734375, 0.0699310302734375]], [[7.747430781700854, 7.7792975485521785, 7.7792975485521785], [0.061676025390625, 0.0699310302734375, 0.0699310302734375]], [[7.747430781700854, 7.747430781700854, 7.7792975485521785], [0.061676025390625, 0.061676025390625, 0.0699310302734375]], [[7.747430781700854, 7.747430781700854, 7.7792975485521785], [0.061676025390625, 0.061676025390625, 0.0699310302734375]], [[7.747430781700854, 7.7792975485521785, 7.797057232181913], [0.061676025390625, 0.0699310302734375, 0.07763671875]]]],
[[[[7.771581898459501, 7.806405402913779], [0.071014404296875, 0.0748443603515625]], [[7.80990384233268], [0.0665740966796875]], [[7.80990384233268, 7.80990384233268], [0.0665740966796875, 0.0665740966796875]], [[7.80990384233268, 7.80990384233268, 7.80990384233268], [0.0665740966796875, 0.0665740966796875, 0.0665740966796875]], [[7.80990384233268, 7.80990384233268, 7.80990384233268], [0.0665740966796875, 0.0665740966796875, 0.0665740966796875]], [[7.80990384233268, 7.80990384233268, 7.80990384233268], [0.0665740966796875, 0.0665740966796875, 0.0665740966796875]]]],
[[[[7.774973994387671, 7.806963312285247], [0.065277099609375, 0.0783538818359375]], [[7.774973994387671, 7.806963312285247], [0.065277099609375, 0.0783538818359375]], [[7.774973994387671, 7.774973994387671, 7.774973994387671], [0.065277099609375, 0.065277099609375, 0.065277099609375]], [[7.774973994387671, 7.774973994387671, 7.7994637252896215], [0.065277099609375, 0.065277099609375, 0.0720977783203125]], [[7.774973994387671, 7.774973994387671, 7.7994637252896215], [0.065277099609375, 0.065277099609375, 0.0720977783203125]], [[7.774973994387671, 7.774973994387671, 7.774973994387671], [0.065277099609375, 0.065277099609375, 0.065277099609375]]]],
[[[[7.7651149849616905, 7.804505385835293], [0.075897216796875, 0.081573486328125]], [[7.7651149849616905, 7.804505385835293, 7.804505385835293], [0.075897216796875, 0.081573486328125, 0.081573486328125]], [[7.789481404079764, 7.804505385835293, 7.804505385835293], [0.0688934326171875, 0.081573486328125, 0.081573486328125]], [[7.804505385835293, 7.804505385835293, 7.804505385835293], [0.081573486328125, 0.081573486328125, 0.081573486328125]], [[7.804505385835293, 7.804505385835293, 7.8212977382836515], [0.081573486328125, 0.081573486328125, 0.1203460693359375]], [[7.804505385835293, 7.804505385835293, 7.8212977382836515], [0.081573486328125, 0.081573486328125, 0.1203460693359375]]]],
[[[[7.73273527823344], [0.0768280029296875]], [[7.7640898495794035], [0.073516845703125]], [[7.7640898495794035, 7.7640898495794035], [0.073516845703125, 0.073516845703125]], [[7.7640898495794035, 7.7640898495794035, 7.7640898495794035], [0.073516845703125, 0.073516845703125, 0.073516845703125]], [[7.7640898495794035, 7.7640898495794035, 7.7640898495794035], [0.073516845703125, 0.073516845703125, 0.073516845703125]], [[7.7640898495794035, 7.7640898495794035, 7.7640898495794035], [0.073516845703125, 0.073516845703125, 0.073516845703125]]]],
[[[[7.737602952804632, 7.740425455598491, 7.740505656220186], [0.066925048828125, 0.0670318603515625, 0.1088104248046875]], [[7.737602952804632, 7.740425455598491, 7.740505656220186], [0.066925048828125, 0.0670318603515625, 0.1088104248046875]], [[7.737602952804632, 7.737602952804632, 7.740425455598491], [0.066925048828125, 0.066925048828125, 0.0670318603515625]], [[7.740425455598491, 7.740425455598491, 7.771720184116807], [0.0670318603515625, 0.0670318603515625, 0.0929107666015625]], [[7.740425455598491, 7.740425455598491, 7.740425455598491], [0.0670318603515625, 0.0670318603515625, 0.0670318603515625]], [[7.740425455598491, 7.740425455598491, 7.740425455598491], [0.0670318603515625, 0.0670318603515625, 0.0670318603515625]]]],
]
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)
    # print(first_pareto_list[0][0][0])# Set up iterator for color plotting.
    # for i in range(len(first_pareto_list)):
    color = iter(plt.cm.jet(np.linspace(0, 1, 2)))
    print(color)
    colors = ['#0000ff', '#6666ff', '#ccccff', '#ffcccc', '#ff6666', '#ff0000']
    # b = list()
    print(len(first_pareto_list))
    # b = b.append(first_pareto_list)
    # print(b)

    # # Get labels for individual fitnesses.
    # ffs = params['FITNESS_FUNCTION'].fitness_functions
    # print (len(first_pareto_list[0][0]))

    # Find the direction for step lines to "bend"
    # step_dir = 'pre' if ffs[0].maximise else 'post'
    step_dir = 'pre'


    # Plot data.
    for y in range (0,30):
            for a in range(0,6):
                for i, gen in enumerate(first_pareto_list[y]):
                    c = colors[a]
                    print(c)
                # print(gen[0]  [0])
                    ax1.step(gen[a][0], gen[a][1], linestyle='-',where=step_dir, color=c, lw=1, alpha=0.8)
                    ax1.plot(gen[a][0], gen[a][1], 'o', color=c, ms=3)

    # Set labels with class names.
    ax1.set_xlabel('8-bit Entropy', fontsize=14)
    ax1.set_ylabel('Autocorrelation', fontsize=14)

    # Plot title and legend.
    # plt.title("First pareto fronts by generation")

    # Set up colorbar instead of legend. Normalise axis to scale of data.
    sm = plt.cm.ScalarMappable(cmap="bwr",
                   norm=plt.Normalize(vmin=0, vmax=6 - 1))

    # Fake up the array of the scalar mappable.
    sm._A = []

    # Plot the colorbar.
    cbar = plt.colorbar(sm, ticks=[0,  5])

    # Set label of colorbar.
    # cbar.ax.get_yaxis().labelpad = 15
    cbar.ax.set_ylabel('Generation', rotation=90)

    # Save plot and close.
    # plt.savefig(path.join(params['FILE_PATH'], "fitness.pdf"))
    plt.savefig("fitness_encorr.svg")
    plt.close()


def save_plot_from_data(data, name):
    """
    Saves a plot of a given set of data.

    :param data: the data to be plotted
    :param name: the name of the data to be plotted.
    :return: Nothing.
    """

    from algorithm.parameters import params

    # Initialise up figure instance.
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)

    # Plot data.
    ax1.plot(data)

    # Set labels.
    ax1.set_ylabel(name, fontsize=14)
    ax1.set_xlabel('Generation', fontsize=14)

    # Plot title.
    plt.title(name)

    # Save plot and close.
    plt.savefig(path.join(params['FILE_PATH'], (name + '.pdf')))
    plt.close()


def save_plot_from_file(filename, stat_name):
    """
    Saves a plot of a given stat from the stats file.

    :param filename: a full specified path to a .csv stats file.
    :param stat_name: the stat of interest for plotting.
    :return: Nothing.
    """

    # Read in the data
    data = pd.read_csv(filename, sep="\t")
    try:
        stat = list(data[stat_name])
    except KeyError:
        s = "utilities.stats.save_plots.save_plot_from_file\n" \
            "Error: stat %s does not exist" % stat_name
        raise Exception(s)

    # Plot the data.
    ax1.plot(stat)

    # Plot title.
    plt.title(stat_name)

    # Get save path
    save_path = pathsep.join(filename.split(pathsep)[:-1])

    # Save plot and close.
    plt.savefig(path.join(save_path, (stat_name + '.pdf')))
    plt.close()


def save_box_plot(data, names, title):
    """
    Given an array of some data, and a list of names of that data, generate
    and save a box plot of that data.

    :param data: An array of some data to be plotted.
    :param names: A list of names of that data.
    :param title: The title of the plot.
    :return: Nothing
    """

    from algorithm.parameters import params

    import matplotlib.pyplot as plt
    plt.rc('font', family='Times New Roman')

    # Set up the figure.
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)

    # Plot tight layout.
    plt.tight_layout()

    # Plot the data.
    ax1.boxplot(np.transpose(data), 1)

    # Plot title.
    plt.title(title)

    # Generate list of numbers for plotting names.
    nums = list(range(len(data))[1:]) + [len(data)]

    # Plot names for each data point.
    plt.xticks(nums, names, rotation='vertical', fontsize=8)

    # Save plot.
    plt.savefig(path.join(params['FILE_PATH'], (title + '.pdf')))

    # Close plot.
    plt.close()

save_pareto_fitness_plot()
