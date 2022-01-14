# Git 명령어

+ 내 컴퓨터에서 최초로 깃-깃허브 매핑 시키는 작업
  + username ,pw
  + chrome 이 좋다(최적화)
    + git / django, javascript, vue 를 chrome에서 작업
  + `git config --global user.username 유저이름`
    + username 등록
    + 유저이름 미입력시 현재 사용자 출력
  + `git config --global user.email 이메일`
    + email 등록
    + 이메일 미입력시 현재 사용 이메일 출력
+ `Working Directory`  즉 내 로컬에서 폴더 만들었을 때 한번 동작
  + `git init` : git 시작
  + `git remote add origin GITURL` : git의 GITURL과 연결
+ `Staging Area(.git)` 작업 할때마다 **계속** 동작
  + `git add .` : 전부 올리기
  + `git add 파일.확장자` : 특정 파일 올리기
  + `git status` : 올린것 확인
  + `git commit -m 'text'` : text 내용을 메세지로 올려준다
  + `git push -u origin master` : commit 내용을 master에서 origin으로 push해서 git에 넣는다
  + `git push` : github에 올려주세요!

### pull/clone

+ `git clone GITURL` : 해당 GITURL을 복사해서 가져옴, 그냥 가져오기만 함
+ `git pull origin master` : 내가 가져온 이 코드를 직접 조지겠다.

### 부가기능

+ `git remote -v` : 등록된 GITURL을 확인하는 용도
+ `Ctrl Shift R` : git 강제 새로고침!
+ `git config --global core.autocrlf true` : 개행 문자 통일