func dfs(course int, graph map[int][]int, visiting map[int]bool) bool {
    if visiting[course] {
        return false
    }
    if len(graph[course]) == 0 {
        return true
    }

    visiting[course] = true
    for _, post := range graph[course] {
        if !dfs(post, graph, visiting) {
            return false
        }
    }
    graph[course] = []int{} // shortcut: return true if ever visited
    visiting[course] = false
    return true
}

func canFinish(numCourses int, prerequisites [][]int) bool {
    graph := make(map[int][]int)
    // Check if there's cycle
    visiting := make(map[int]bool)
    // build the graph
    for _, tuple := range prerequisites {
        graph[tuple[1]] = append(graph[tuple[1]], tuple[0])
        visiting[tuple[1]] = false
    }
    // fmt.Printf("%v\n", graph)

    for c := range numCourses {
        if !dfs(c, graph, visiting) {
            return false
        }
    }

    return true
}
