<template>
	<nav class="nav-links">
		<ul>
			<li>
				<i class="las la-user-circle" style="font-size: 28px"></i>
				<NuxtLink
				to="/about-me"
				rel="next author noreferrer noopener"
				class="cursor-hover"
				:style="{
						textDecoration:
							$route.path === '/about-me' || !$route.path
								? 'underline'
								: 'none',
					}"
				>
					<span>About Me</span>
				</NuxtLink>
			</li>
			<li>
				<i class="las la-briefcase" style="font-size: 28px"></i>
				<NuxtLink
					to="/work"
					exact
					rel="next author noreferrer noopener"
					class="cursor-hover"
					:style="{
						textDecoration:
							$route.path === '/work' ? 'underline' : 'none',
					}"
				>
					<span>Work</span>
				</NuxtLink>
			</li>
			<li>
				<i class="las la-project-diagram" style="font-size: 28px"></i>
				<NuxtLink
					to="/projects"
					exact
					rel="next author noreferrer noopener"
					class="cursor-hover"
					:style="{
						textDecoration:
							$route.path === '/projects' ? 'underline' : 'none',
					}"
				>
					<span>Projects</span>
				</NuxtLink>
			</li>
			<!-- <li>
				<i class="las la-chart-bar" style="font-size: 28px" />
				<NuxtLink
					to="/analytics-by-jay"
					exact
					rel="next author noreferrer noopener"
					class="cursor-hover"
					:style="{
							textDecoration:
									$route.path === '/analytics-by-jay'
											? 'underline'
											: 'none',
					}"
				>
				<span>
						Analytics by Jay
					</span>
				</NuxtLink>
			</li> -->
		</ul>
	</nav>
</template>

<script>
import { ref, onMounted } from "vue";
import { useRoute, useRouter, onBeforeRouteUpdate } from "vue-router";

export default {
    setup() {
        const route = useRoute();
        const router = useRouter();
        const activeLink = ref(null);

        onBeforeRouteUpdate((to, from) => {
            console.warn("navigation-to", to);
            console.warn("navigation-from", from);
            console.warn("route-data", route);
        });

        // Check if the current URL ends with "index.html"
        // if (currentUrl.endsWith("index.html") || currentUrl.endsWith("/")) {
        //   // If yes, set the text-decoration of the element with href "index.html" to "underline"
        //   // since we currently have two html files in the root directory
        //   // simple if-else statement is fine
        //   document.querySelector("a[href='index.html']").style.textDecoration = "underline";
        // } else if (currentUrl.endsWith("work.html")) {
        //   document.querySelector("a[href='work.html']").style.textDecoration = "underline";
        // } else if (currentUrl.endsWith("projects.html")) {
        //   // If not, set the text-decoration of the element with ID "my-link" to "none"
        //   document.querySelector("a[href='projects.html']").style.textDecoration = "underline";
        // }

        return {
            activeLink,
        };
    },
};
</script>

<style scoped>
.active-link {
    text-decoration: underline;
}

@media screen and (max-width: 640px) {
	nav.nav-links {
		position: static;
	}

	nav.nav-links > ul {
		border: none;
		display: flex;
		flex-direction: row;
		justify-content: space-around;

		padding-left: 0;
		overflow-y: hidden;
		overflow-x: scroll;
	}

	nav.nav-links > ul > li > a {
		font-size: 16px;
	}

	::-webkit-scrollbar {
		display: none;
	}
}

@media screen and (min-width: 640px) and (max-width: 768px) {
    nav.nav-links > ul > li > a {
        font-size: 20px;
    }
}
</style>
