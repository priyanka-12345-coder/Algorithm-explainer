from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/explain', methods=['POST'])
def explain_algorithm():
    try:
        # Getting data from frontend
        data = request.get_json()
        algorithm_name = data.get('algorithmName')
        user_level = data.get('userLevel')
        language = data.get('language')

        # Validate if all required fields are provided
        if not algorithm_name or not user_level or not language:
            return jsonify({'error': 'Missing required fields'}), 400

        # Simulated explanation logic based on the selected algorithm
        explanation = {
            "Algorithm": algorithm_name,
            "Level": user_level,
            "Step-by-step": f"Step-by-step explanation of {algorithm_name} for {user_level} user.",
            "Pseudocode": get_pseudocode(algorithm_name),
            "Time Complexity": "O(N log N) (example)",
            "Real-World Example": f"A real-world analogy for {algorithm_name}.",
            "Code": get_code(algorithm_name, language)
        }

        return jsonify(explanation)

    except Exception as e:
        # Log error and return generic error message
        print(f"Error: {str(e)}")
        return jsonify({'error': 'Something went wrong. Please try again later.'}), 500

# Function to get pseudocode (Simulated logic)
def get_pseudocode(algorithm_name):
    if algorithm_name == "Dijkstra":
        return """1. Initialize distances to all vertices as infinity.
2. Set distance to the source vertex as 0.
3. Mark all vertices as unvisited.
4. For the unvisited vertex with the smallest distance, consider its unvisited neighbors.
5. Calculate tentative distances and update if smaller.
6. Repeat until all vertices are visited."""
    elif algorithm_name == "Bubble Sort":
        return """1. Compare each pair of adjacent elements.
2. If they are in the wrong order, swap them.
3. Repeat the process until the array is sorted."""
    else:
        return "Pseudocode for this algorithm is not available."

# Function to get code in the desired language (Simulated logic)
def get_code(algorithm_name, language):
    if algorithm_name == "Dijkstra":
        if language == "Python":
            return """import heapq
def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    pq = [(0, start)]
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances"""
        elif language == "JavaScript":
            return """function dijkstra(graph, start) {
                let distances = {};
                for (let vertex in graph) {
                    distances[vertex] = Infinity;
                }
                distances[start] = 0;
                let pq = [[0, start]];
                while (pq.length > 0) {
                    let [currentDistance, currentVertex] = pq.pop();
                    for (let [neighbor, weight] of graph[currentVertex]) {
                        let distance = currentDistance + weight;
                        if (distance < distances[neighbor]) {
                            distances[neighbor] = distance;
                            pq.push([distance, neighbor]);
                        }
                    }
                }
                return distances;
            }"""
        else:
            return "Code for this algorithm in the selected language is not available."
    elif algorithm_name == "Bubble Sort":
        if language == "Python":
            return """def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr"""
        elif language == "JavaScript":
            return """function bubbleSort(arr) {
                for (let i = 0; i < arr.length; i++) {
                    for (let j = 0; j < arr.length - i - 1; j++) {
                        if (arr[j] > arr[j+1]) {
                            [arr[j], arr[j+1]] = [arr[j+1], arr[j]];
                        }
                    }
                }
                return arr;
            }"""
        else:
            return "Code for this algorithm in the selected language is not available."
    else:
        return "Code for this algorithm is not available in the selected language."

if __name__ == '__main__':
    app.run(debug=True)



