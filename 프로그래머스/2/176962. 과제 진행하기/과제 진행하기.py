def solution(plans):
    # 과제들을 시작 시간이 빠른 순서대로 정렬합니다.
    plans.sort(key=lambda x: x[1])

    result = []  # 완료된 과제들을 순서대로 저장할 리스트
    paused_tasks = []  # 멈춘 과제들을 저장할 스택
    current_time = 0  # 현재 시간을 초기화

    for task_name, start_time, duration in plans:
        # 시작 시간을 분 단위로 변환 (hh:mm 형식)
        start_hour, start_minute = map(int, start_time.split(":"))
        start_in_minutes = start_hour * 60 + start_minute

        # 현재 과제와 새로운 과제 시작 시간 사이의 여유 시간을 계산
        if current_time < start_in_minutes:
            available_time = start_in_minutes - current_time
            
            # 여유 시간 동안 멈춘 과제들을 이어서 진행
            while paused_tasks and available_time > 0:
                paused_task_name, remaining_time = paused_tasks.pop()
                if available_time >= remaining_time:
                    # 멈춘 과제를 다 끝낼 수 있는 경우
                    result.append(paused_task_name)
                    available_time -= remaining_time
                else:
                    # 멈춘 과제를 다 끝낼 수 없는 경우, 남은 시간 업데이트
                    paused_tasks.append((paused_task_name, remaining_time - available_time))
                    available_time = 0

        # 현재 시간을 새로운 과제의 시작 시간으로 업데이트
        current_time = start_in_minutes

        # 새로운 과제를 남은 시간과 함께 스택에 추가
        remaining_duration = int(duration)
        paused_tasks.append((task_name, remaining_duration))

    # 모든 과제를 확인한 후 남아있는 멈춘 과제를 순서대로 처리
    while paused_tasks:
        result.append(paused_tasks.pop()[0])

    return result