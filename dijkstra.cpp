#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <bits/stdc++.h>
using namespace std;

int minDistance(int dist[], bool sptSet[], int N)
{
    int min = INT_MAX, min_index;

    for (int v = 0; v < N; v++)
        if (sptSet[v] == false && dist[v] <= min)
            min = dist[v], min_index = v;

    return min_index;
}

void dijkstra(vector<vector<int>> map, int N, int S)
{
    int dist[N];

    bool set[N];

    int pred[N];

    for (int i = 0; i < N; i++)
    {
        dist[i] = INT_MAX;
        set[i] = false;
    }

    dist[S] = 0;
    pred[S] = 0;
    cout << "Node: ";
    for (int i = 0; i < N; i++)
    {
        cout << "  " << i << "  ";
    }
    cout << "\n";
    for (int count = 0; count < N - 1; count++)
    {
        cout << "Iter #" << count + 1 << " ";
        int u = minDistance(dist, set, N);

        set[u] = true;
        for (int v = 0; v < N; v++)
            if (!set[v] && map[u][v] && dist[u] != INT_MAX && dist[u] + map[u][v] < dist[v])
            {
                dist[v] = dist[u] + map[u][v];
                pred[v] = u;
            }
        for (int v = 0; v < N; v++)
        {
            if (dist[v] == INT_MAX)
            {
                cout << " -  ";
            }
            else
            {
                cout << dist[v] << ";" << pred[v] << " ";
            }
        }
        cout << "\n";
    }
}

int main()
{
    int N;
    int S;
    cout << "Number of vertices: ";
    cin >> N;
    cout << "Input source node: ";
    cin >> S;
    vector<vector<int>> map;
    map.resize(N);
    for (int i = 0; i < N; i++)
    {
        map[i].resize(N);
    };
    for (int i = 0; i < N; i++)
    {
        cout << "Input the weight to travel from vertex " << i << " to all other verticies seperated by a space: ";
        for (int j = 0; j < N; j++)
        {
            cin >> map[i][j];
        }
    };

    dijkstra(map, N, S);
    return 0;
}