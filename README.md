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
      <td>"이미지 데이터 전처리" - <b>[문성우](https://github.com/Leo-Moooon)</b></td>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        이미지 분류를 주제로 시행하는 미니 프로젝트다보니 다음의 2가지에 초점을 맞췄습니다.<br>
       1. 객체인식 모델을 쓸 수 없는 제한적 상황에서 올바른 학습을 위해 데이터 내 노이즈 최소화<br>
       2. 협업환경이 구글 드라이브, 코랩인 점을 감안하여 데이터 업로드, 다운로드 간 소요시간 최소화<br><br>
      이를 위해 이미지 크롭과 오픈소스 모델을 이용한 오브젝트 외 영역 마스킹을 시도했습니다.<br>
      사진 속 인물의 전체적인 착장을 보고 라벨(스타일)을 예측해야 하는 상황에서 각 오브젝트를 분리하지 않았을 때 제대로된 학습이 이루어지지 않았기 때문에, 원본 이미지와 함께 각 오브젝트끼리 분리한 이미지를 함께 넣어 학습에 도움이 될 것이라는 가설에서 위 2가지 방법을 선정했습니다.<br>
      아쉽게도 모델의 성능을 극적으로 끌어올릴 수는 없었으나, 이미지 크롭보다 오브젝트별 마스킹 시 학습의 양상이 더 긍정적인 것을 확인할 수 있었습니다.<br>
      추가로, 구글 드라이브+코랩을 협업환경으로 사용하는 중에 구글 드라이브의 서버 오류로 예기치 못한 사고를 더러 겪으면서 프로젝트 시간을 많이 뺏긴 것이 너무 아쉽습니다.<br>
      </td>
    </tr>
  </tbody>
</table>
<br>
<table>
  <thead>
    <tr>
      <td>"모델링, 하이퍼파라미터 튜닝" - <b>[채성혁](https://github.com/xxonyuk)</b></td>
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
      <td>"이미지 데이터 크롤링, 모델 서빙, 웹 서비스 제작" - <b>[윤인수](https://github.com/F4ctor-Yoon)</b></td>
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
<br>
<table>
  <thead>
    <tr>
      <td>"이미지 크롭, 모델 & 전처리 서칭" - <b>[신준섭](https://github.com/A1zania)</b></td>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        기존 트레인 데이터와 별개로 조원끼리 나누어 크롤링한 사진들을 바탕으로, 의류를 강조하는 크롭을 진행하여 타겟을 보다 확실하게 했습니다. 또한 크롭한 이미지들에 의류 정보를 라벨링하여 학습에 도움이 되도록 했습니다.<br>
        최초로 전달 드린 모델인 vgg19가 너무 오래 걸린다는 의견을 주셔서 경량화 모델을 위주로 서칭 하였고, 바로 적용 및 커스텀을 가능하시게 하기 위해 paper review와 예시 코드들을 같이 전달 드렸습니다.. (GoogLeNet 기반의 inception v4 small_ver, efficientnet v2)<br>
        그러나 해당 모델들은 가볍긴 했으나 좋은 퍼포먼스를 보이지 못했습니다. 따라서 accuracy를 올리기 위한 방안을 구상했습니다.<br>
        기존의 의류 도메인의 정보를 가지고 있는 모델을 사용한다면 보다 트레인이 잘 될 것이라 생각하여 의류 모델 도메인 정보가 들어가 있는 vgg-16기반의 FashionNet과 BCRNN을 찾아서 관련 정보를 전달드렸습니다.<br>
        이번 프로젝트를 진행하며 얻은 지식으로는 굳이 무거운 모델이 아니더라도 비슷한 성능을 내는 경량화 모델들이 다수 존재하고 있음을 알게 되었으며, 추후 다른 프로젝트를 진행하게 될 때도 하드웨어의 상황에 맞게 다양한 모델을 제시 할 수 있는 정보를 얻게 되었던 것 같습니다.<br>
        다만 이러한 다양한 고성능의 모델이 있음에도 불구하고 23개의 분류를 진행하는 것은 상당히 힘들며, 상위 카테고리를 만들어 1차 분류를 하고 이를 통한 전이학습이 보다 효과적일 수 있다는 교훈을 얻게 되었던 것 같습니다.
      </td>
    </tr>
  </tbody>
</table>
<br>
<table>
  <thead>
    <tr>
      <td>"이미지 크롭" - <b>[홍영택](https://github.com/hytgithub007)</b></td>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        크롭 도중 사이즈만 다르고 중복되는 이미지를 크롭할 때 과연 이 이미지를 크롭 해야 하는가 라는 고민을 했고, 일일히 그림판이나 편집 등으로 이미지를 크롭 하지 않고 라벨링 프로그램이나 내가 하는 작업을 수월하게 하는 프로그램이나 코드가 있지 않을까 라는 생각을 했습니다.<br>
        사이즈가 다른 이미지 또한 다른 이미지라고 생각하여 크롭을 진행했습니다.<br>
        이미지를 크롭하는 프로그램이나 코드를 찾는 것보다 그 시간에 이미지를 크롭하는게 더 낫다는 생각을 하여 크롭에 도움이 되는 프로그램이나 코드를 찾기보다 하던대로 그림판을 이용해 이미지 크롭에 더 집중했습니다.<br>
        추후에는 다음 프로젝트 때는 도움이 되는 프로그램이나 작업에 대한 노하우를 찾아 작업 시간을 줄이는 방향으로 진행하겠습니다.
      </td>
    </tr>
  </tbody>
</table>
<hr>

## AI HUB 데이터 K-Fashion 이미지 데이터를 사용한 스타일 분류 모델 개발 리더보드 챌린지
![result](https://github.com/F4ctor-Yoon/k-fashion/assets/13534979/dc3c2314-0115-4cdf-873c-294c993dcd81)<br>


