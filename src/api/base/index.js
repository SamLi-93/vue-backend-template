import request from '@/utils/request'

export function getUserMenuList() {
  return request({
    url: '/user/menu',
    method: 'get',
  })
}

