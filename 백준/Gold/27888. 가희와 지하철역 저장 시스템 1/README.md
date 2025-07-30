# [Gold II] 가희와 지하철역 저장 시스템 1 - 27888 

[문제 링크](https://www.acmicpc.net/problem/27888) 

### 성능 요약

메모리: 101612 KB, 시간: 2040 ms

### 분류

구현, 자료 구조, 문자열, 집합과 맵, 비트마스킹, 해시를 사용한 집합과 맵, 파싱

### 제출 일자

2025년 7월 30일 23:01:17

### 문제 설명

<p>가희는 <code>n</code>개의 지하철역 정보를 보기 위한 시스템을 만들었습니다. 이 시스템은 정말 단순하게 동작합니다.</p>

<ul>
	<li>유저가 역 <code>station</code>의 특징을 한 번도 업데이트하지 않은 경우, 역 <code>station</code>의 특징은 없습니다.</li>
	<li>각 역은 유저들이 업데이트한 특징이 있습니다. 예를 들어, <code>deepstation</code>, <code>longescalator</code>, <code>dungeon</code>과 같은 것들입니다.</li>
	<li><code>deepstation</code>, <code>longescalator</code>, <code>dungeon</code>과 같은 특징을 입력했을 때 조건에 맞는 역들이 나타나게 됩니다.</li>
</ul>

<p>그런데 사용하는 유저가 많아질수록 가희가 만들어 놓은 시스템이 느려지기 시작했습니다. 가희를 도와주세요.</p>

### 입력 

 <p>첫 번째 줄에 <code>n</code>이 주어집니다.</p>

<p>다음 <code>n</code>개의 줄에 역 이름이 <strong>한 줄에 하나씩</strong> 주어집니다.</p>

<p>다음 줄에 요청의 개수 <code>r</code>이 주어집니다.</p>

<p>다음 <code>r</code>개의 줄에 요청이 다음 형식 중 하나로 주어집니다.</p>

<ul>
	<li><code>U</code> <code>station</code> <code>features</code>

	<ul>
		<li>역 <code>station</code>의 특징을 <code>features</code>로 업데이트합니다.</li>
	</ul>
	</li>
	<li><code>G</code> <code>features</code>
	<ul>
		<li><code>features</code>의 특징을 <strong>모두 가진</strong> 역의 개수를 출력합니다.</li>
	</ul>
	</li>
</ul>

<p>이때 <code>features</code>는 특징이 여러 개인 경우 <strong>콤마(<span style="color:#E74C3C;"><code>,</code></span>)로 구분되어</strong> 주어집니다. 또한 중복된 특징은 주어지지 않습니다.</p>

<p><code>station</code>은 주어진 <code>n</code>개의 지하철역 이름 중 하나입니다..</p>

<p>예를 들어, <code>soongsiluniv</code>역의 특징을 <code>line7</code>과 <code>deep</code>으로 업데이트 하려는 경우 요청은 아래와 같이 주어집니다.</p>

<p style="text-align: center;"><code>U soongsiluniv</code> <code>line7,deep</code></p>

<p>또한 특징 <code>beautiful</code>과 <code>dungeon</code>이라는 특징을 가지는 역의 개수를 구하라는 요청은 아래와 같이 주어집니다.</p>

<p style="text-align: center;"><code>G</code> <code>beautiful,dungeon</code></p>

### 출력 

 <p>조건을 만족하는 역의 개수를 구하라는 요청이 들어올 때마다 한 줄에 하나씩 답을 출력해 주세요.</p>

