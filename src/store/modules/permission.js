import { getUserMenuList } from '@/api/base/index'
import { recursionRouter } from '@/utils/menuUtil'
import {asyncRouterMap, constantRouterMap} from '@/router/index'
import Router from 'vue-router'
import router from '@/router/index'

const permission = {
  state: {
    permissionList: [] /** 所有路由 */,
    sidebarMenu: [] /** 导航菜单 */,
    currentMenu: '' /** 当前active导航菜单 */
  },

  mutations: {
    SET_USERMENULIST: (state, menuList) => {
      state.permissionList = menuList
    },
  },

  actions: {
    // 获取用户菜单列表信息
    getMenu({ commit, state }) {
      return new Promise((resolve, reject) => {
        getUserMenuList().then(response => {
          const data = response.data
          if (data.menuList && data.menuList.length > 0) { // 验证返回的name是否是一个非空数组
            // commit('SET_USERMENULIST', data.menuList)
            let permissionList = data.menuList
            let routes = recursionRouter(permissionList, asyncRouterMap)
            // let MainContainer = asyncRouterMap
            // let children = MainContainer.children
            // children.push(...routes)
            // console.log(routes)

            router.addRoutes(routes)
            // console.log(router.options.routes)
            let initialRoutes = router.options.routes
            commit('SET_USERMENULIST', [...initialRoutes, ...routes])
          } else {
            reject('getMenu: menuList must be a non-null array !')
          }
          resolve(response)
        }).catch(error => {
          reject(error)
        })
      })
    },
  }
}

export default permission
