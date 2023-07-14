# k-fashion(스타일 분류 모델 개발)

![image](https://github.com/F4ctor-Yoon/k-fashion/assets/13534979/3f38d739-741e-4ff3-accf-635d2db56435)


<div>
  <h3>Model</h3>
  <img src="https://img.shields.io/badge/-Python-3776AB?style=flat&logo=Python&logoColor=white"/>
  <img src="https://img.shields.io/badge/-Tensorflow-FF6F00?style=flat&logo=Tensorflow&logoColor=white"/>
  <img src="https://img.shields.io/badge/-Keras-D00000?style=flat&logo=Keras&logoColor=white"/>
  <img src="https://img.shields.io/badge/-NumPy-013243?style=flat&logo=NumPy&logoColor=white"/>
  <img src="https://img.shields.io/badge/-Pandas-150458?style=flat&logo=Pandas&logoColor=white"/>
  <br>
  사용한 데이터 : <a href="https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=51">AI HUB K-Fashion 이미지</a>
</div>

<h3>Serving/Web</h3>
<div>
  <img src="https://img.shields.io/badge/-Flask-000000?style=flat&logo=Flask&logoColor=white"/>
  <img src="https://img.shields.io/badge/-HTML-E34F26?style=flat&logo=HTML5&logoColor=white"/>
  <img src="https://img.shields.io/badge/-CSS-1572B6?style=flat&logo=CSS3&logoColor=white"/>
  <img src="https://img.shields.io/badge/-JavaScript-F7DF1E?style=flat&logo=JavaScript&logoColor=white"/>
  <img src="https://img.shields.io/badge/-Bootstrap-7952B3?style=flat&logo=Bootstrap&logoColor=white"/>
</div>
<hr>
<table>
  <thead>
    <tr>
      <td>"모델링, 하이퍼파라미터 튜닝" - <b>채성혁</b></td>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        inceptionnet3,4, efficientnetv2l, b0, b7 vgg16,19 resnet50 등 이미지 분류에서 sota를 찍었던 모델들을 많이 사용해보았으나 vgg19, resnet50말곤 학습조차 되지않은 경향을 보였습니다.<br>
        조금이라도 학습이되게 할수있었던 방향은 처음엔 lr 을 크게 가주면서 10에폭마다 0.5를 곱하면서 떨어트린것 즉 lr를 줄일수록 큰 학습효과를 가져왔습니다.<br>
        그마저 vgg19, resnet50이 학습이된다하더라고 acc는 최고 0.2 정도 매우 저조한 성능을 나타냈습니다.<br>
        pretrained 모델을 불러와서 쓰면서 출력층을 Dense 층을 2개 쌓고 dropout한거보다 그냥 바로 23개로 분류하는것이 보다 효과적이였습니다.<br>
        23개를 분류하는거 자체가 모델에겐 너무 힘들일이여서 성능이 안나왔던거같습니다.<br>
        다음에 하게된다면 상,하의 따로 구분해서 하거나 카테고리를 23개에서 보다 상위 분류로 해서 카테고리를 줄이는 방향으로 진행해야될거같습니다.
      </td>
    </tr>
  </tbody>
</table>
<br>
<table>
  <thead>
    <tr>
      <td>"모델 서빙, 웹 서비스 제작" - <b>윤인수</b></td>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        원하는 부분만 크롭하여 사용하면, 분류를 더 잘하지 않을까 싶어 <a href="https://github.com/fengyuanchen/cropperjs">Cropper.js</a>를 사용였습니다.<br>
        Inference까지 이미지 파일을 어떻게 전달할지가 고민이었습니다. input type을 file로 하고 submit 하는 방법도 있지만, 페이지 이동으로 흐름이 끊겨 사용자 경험 면에서 안 좋다 생각하였습니다.<br>
        고민 끝에, ajax를 사용해 비동기로 이미지 파일을 전송하고, 스타일 분류 결과를 돌려받는 식으로 처리하였습니다.
      </td>
    </tr>
  </tbody>
</table>
<hr>

## [AI HUB 데이터 K-Fashion 이미지 데이터를 사용한 스타일 분류 모델 개발 리더보드 챌린지](https://competition.aihub.or.kr/hackathon/scheduleDetail/5)
![image](https://github.com/F4ctor-Yoon/k-fashion/assets/13534979/731b5409-2ab4-4bc5-85ea-e0d68b21cf21)<br>

