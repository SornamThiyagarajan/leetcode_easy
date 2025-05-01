from collections import deque 
class Solution:

   def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        #step1: Sort task and workers
        tasks.sort()
        workers.sort()

        ##step2: Binary Search to find the max no of tasks that can be assinged
        def can_assign(k):
            dq = deque()
            i = len(workers)-1
            remaining_pills = pills 

            ##Step3: Assign k hardest task 
            for j in range(k-1, -1, -1):
                while(i>= len(workers)-k and workers[i] + strength >=tasks[j] ):
                    dq.appendleft(workers[i])
                    i -= 1 

                if not dq: 
                    return False 

                if dq[-1] >= tasks[j]:
                    dq.pop()

                elif remaining_pills > 0: 
                    dq.popleft()
                    remaining_pills -= 1 

                else: 
                    return False 

            return True 

        low,high=0, min(len(tasks),len(workers))
        ans = 0 

        while(low<=high):
            mid = (low+high)//2
            if can_assign(mid):
                answer = mid 
                low = mid+1
            else: 
                high = mid -1
            
        
        return answer 
