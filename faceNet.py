from main import ageModel, ageProto, args, faceModel, faceProto 


import cv2


faceNet=cv2.dnn.readNet(faceModel,faceProto)
ageNet=cv2.dnn.readNet(ageModel,ageProto)
video=cv2.VideoCapture(args.image if args.image else 0)