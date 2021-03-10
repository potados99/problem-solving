/**
 * 18224번: 미로에 갇힌 건우
 * https://www.acmicpc.net/problem/18224
 */

#include <cstdio>
#include <queue>

using namespace std;

int n, m;
int maze[500][500];
int visited[500][500][11][2];

int dx[] = {-1, 0, 1, 0};
int dy[] = {0, -1, 0, 1};

struct Node {
    int x;
    int y;
    int count;
};

static inline int tickToDate(int tick) {
    return tick / (2*m) + 1;
}

static inline int tickToDaynight(int tick) {
    return (tick / m) % 2;
}

int bfs() {
    queue<Node> q;

    q.push({0, 0, 0});
    visited[0][0][0][0] = true;

    while (!q.empty()) {
        Node cur = q.front();
        q.pop();

        int x = cur.x;
        int y = cur.y;
        int count = cur.count;
        int daynight = tickToDaynight(cur.count);

        if (x == n-1 && y == n-1) {
            return count;
        }

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            int nCount = (count + 1) % m;
            int nDaynight = tickToDaynight(count + 1);

            if (nx < 0 | ny < 0 || nx >= n || ny >= n || visited[nx][ny][nCount][nDaynight]) {
                continue;
            }

            if (maze[nx][ny] == 1) {
                if (daynight == 0) {
                    continue;
                }

                while (true) {
                    nx += dx[i];
                    ny += dy[i];

                    if (nx < 0 | ny < 0 || nx >= n || ny >= n || visited[nx][ny][nCount][nDaynight]) {
                        break;
                    } else if (maze[nx][ny] == 0) {
                        visited[nx][ny][nCount][nDaynight] = true;
                        q.push({nx, ny, count + 1});
                        break;
                    }
                }
            } else {
                visited[nx][ny][nCount][nDaynight] = true;
                q.push({nx, ny, count + 1});
            }
        }
    }

    return -1;
}

int main() {
    scanf("%d %d", &n, &m);

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%d", &maze[i][j]);
        }
    }

    int count = bfs();

    if (count > -1) {
        printf("%d %s\n", tickToDate(count), tickToDaynight(count) ? "moon" : "sun");
    } else {
        printf("-1\n");
    }

    return 0;
}
