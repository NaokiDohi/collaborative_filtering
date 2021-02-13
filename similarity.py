import math

coppola_brando = [(5.00, 5.00),(5.00, 4.29)]
coppola_dreyfuss = [(5.00, 1.07),(5.00, 0.63)]
really_liked = [(5.00, 5.00),(5.00, 5.00)]

# ユーグリッド距離
def euclidean_distance(points):
	# for point in points:
	# 	print(point[0])
	# 	print(point[1])
	squared_diffs = [(point[0] - point[1]) ** 2 for point in points]
	summed_squared_diffs = sum(squared_diffs)
	distance = math.sqrt(summed_squared_diffs)
	return distance

def similarity(points):
	# 1を分母に加算したのは同じ数字の時に0で割るのを避ける為
	# 1に近いほど似ている
	return 1/(1 + euclidean_distance(points))

print("coppola_brando:{}".format(similarity(coppola_brando)))
print("coppola_dreyfuss:{}".format(similarity(coppola_dreyfuss)))
print("really_liked:{}".format(similarity(really_liked)))
